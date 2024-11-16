from flask import Blueprint, request, jsonify, send_file, current_app
from werkzeug.utils import secure_filename
from ..pipeline import CryptoPipeline
import os
from datetime import datetime
import json
from pathlib import Path
import shutil
import tempfile
import uuid

bp = Blueprint('crypto', __name__)
pipeline = CryptoPipeline()

DOWNLOAD_FOLDER = 'downloads'

def ensure_folders_exist():
    if not os.path.exists(DOWNLOAD_FOLDER):
        os.makedirs(DOWNLOAD_FOLDER)

def generate_unique_filename(original_filename, prefix=''):
    """Generate a unique filename with optional prefix"""
    name, ext = os.path.splitext(secure_filename(original_filename))
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    unique_id = uuid.uuid4().hex[:8]
    return f"{prefix}{name}_{timestamp}_{unique_id}{ext}"

def cleanup_old_files():
    current_time = datetime.now().timestamp()
    for filename in os.listdir(DOWNLOAD_FOLDER):
        filepath = os.path.join(DOWNLOAD_FOLDER, filename)
        if os.path.isfile(filepath):
            file_time = os.path.getmtime(filepath)
            if current_time - file_time > 3600:  # 1 hour
                os.remove(filepath)

@bp.route('/encrypt', methods=['POST'])
def encrypt_file():
    ensure_folders_exist()
    cleanup_old_files()

    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    try:
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            file.save(temp_file.name)
            
            # Encrypt file
            encrypted_path, key_path = pipeline.encrypt_file(temp_file.name)
            
            # Generate unique filenames
            download_encrypted = os.path.join(DOWNLOAD_FOLDER, 
                generate_unique_filename(file.filename, prefix='encrypted_'))
            download_keys = os.path.join(DOWNLOAD_FOLDER, 
                generate_unique_filename(file.filename, prefix='keys_'))
            
            # Move files to download folder
            shutil.move(encrypted_path, download_encrypted)
            shutil.move(key_path, download_keys)
            
        os.unlink(temp_file.name)
        
        return jsonify({
            'message': 'Encryption successful',
            'encrypted_file_url': f'/download/{os.path.basename(download_encrypted)}',
            'keys_file_url': f'/download/{os.path.basename(download_keys)}'
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/decrypt', methods=['POST'])
def decrypt_file():
    ensure_folders_exist()
    cleanup_old_files()

    if 'encrypted_file' not in request.files or 'key_file' not in request.files:
        return jsonify({'error': 'Both encrypted file and key file are required'}), 400
    
    encrypted_file = request.files['encrypted_file']
    key_file = request.files['key_file']
    
    if encrypted_file.filename == '' or key_file.filename == '':
        return jsonify({'error': 'Both files must be selected'}), 400
    
    try:
        with tempfile.NamedTemporaryFile(delete=False) as temp_encrypted, \
             tempfile.NamedTemporaryFile(delete=False, suffix='.json') as temp_keys:
            
            encrypted_file.save(temp_encrypted.name)
            key_file.save(temp_keys.name)
            
            decrypted_path = pipeline.decrypt_file(temp_encrypted.name, temp_keys.name)
            
            # Generate unique filename for decrypted file
            download_path = os.path.join(DOWNLOAD_FOLDER, 
                generate_unique_filename(encrypted_file.filename, prefix='decrypted_'))
            
            shutil.move(decrypted_path, download_path)
            
        os.unlink(temp_encrypted.name)
        os.unlink(temp_keys.name)
        
        return jsonify({
            'message': 'Decryption successful',
            'decrypted_file_url': f'/download/{os.path.basename(download_path)}'
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/download/<filename>')
def download_file(filename):
    try:
        file_path = os.path.join(DOWNLOAD_FOLDER, filename)
        if not os.path.exists(file_path):
            return jsonify({'error': 'File not found'}), 404

        mimetype = 'application/json' if filename.startswith('keys_') else None
        
        return send_file(
            file_path,
            mimetype=mimetype,
            as_attachment=True,
            download_name=filename
        )
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500