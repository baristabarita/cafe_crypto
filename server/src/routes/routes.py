from flask import Blueprint, request, jsonify
from ..pipeline import CryptoPipeline
import os

bp = Blueprint('crypto', __name__)
pipeline = CryptoPipeline()

@bp.route('/encrypt', methods=['POST'])
def encrypt_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    # Save uploaded file temporarily
    temp_path = f"temp_{file.filename}"
    file.save(temp_path)
    
    try:
        # Encrypt file
        encrypted_path, key_path = pipeline.encrypt_file(temp_path)
        
        # Read encrypted file and keys
        with open(encrypted_path, 'rb') as f:
            encrypted_data = f.read()
        with open(key_path, 'r') as f:
            keys = f.read()
        
        # Clean up
        os.remove(temp_path)
        os.remove(encrypted_path)
        os.remove(key_path)
        
        return jsonify({
            'encrypted_file': encrypted_data.hex(),
            'keys': keys
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/decrypt', methods=['POST'])
def decrypt_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No encrypted file provided'}), 400
    
    if 'keys' not in request.files:
        return jsonify({'error': 'No keys file provided'}), 400
    
    encrypted_file = request.files['file']
    keys_file = request.files['keys']
    
    # Save files temporarily
    temp_encrypted = f"temp_encrypted_{encrypted_file.filename}"
    temp_keys = f"temp_keys_{keys_file.filename}"
    
    encrypted_file.save(temp_encrypted)
    keys_file.save(temp_keys)
    
    try:
        # Decrypt file
        decrypted_path = pipeline.decrypt_file(temp_encrypted, temp_keys)
        
        # Read decrypted file
        with open(decrypted_path, 'rb') as f:
            decrypted_data = f.read()
        
        # Clean up
        os.remove(temp_encrypted)
        os.remove(temp_keys)
        os.remove(decrypted_path)
        
        return jsonify({
            'decrypted_file': decrypted_data.hex()
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500