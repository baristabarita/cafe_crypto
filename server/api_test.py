# test_api.py
import requests
import os
import json
from pathlib import Path

def test_api():
    # Create test files directory if it doesn't exist
    if not os.path.exists('test_files'):
        os.makedirs('test_files')
    
    # Create a test file
    test_file_path = 'test_files/logo(1).png'
    with open(test_file_path, 'wb') as f:
        f.write(b"This is a test file for API testing!\nMultiple lines!\n123456789")
    
    print(f"Created test file: {test_file_path}")
    
    BASE_URL = 'http://localhost:5000/api'
    
    try:
        # Test encryption
        print("\nTesting encryption endpoint...")
        with open(test_file_path, 'rb') as f:
            files = {'file': ('test.txt', f)}
            response = requests.post(f'{BASE_URL}/encrypt', files=files)
        
        if response.status_code == 200:
            print("✅ Encryption successful!")
            data = response.json()
            
            # Save encrypted file and keys for decryption test
            encrypted_data = bytes.fromhex(data['encrypted_file'])
            with open('test_files/encrypted.bin', 'wb') as f:
                f.write(encrypted_data)
            
            with open('test_files/keys.json', 'w') as f:
                f.write(data['keys'])
            
            print("Saved encrypted file and keys")
            
            # Test decryption
            print("\nTesting decryption endpoint...")
            with open('test_files/encrypted.bin', 'rb') as ef, \
                 open('test_files/keys.json', 'rb') as kf:
                files = {
                    'file': ('encrypted.bin', ef),
                    'keys': ('keys.json', kf)
                }
                response = requests.post(f'{BASE_URL}/decrypt', files=files)
            
            if response.status_code == 200:
                print("✅ Decryption successful!")
                data = response.json()
                
                # Save decrypted file
                decrypted_data = bytes.fromhex(data['decrypted_file'])
                with open('test_files/decrypted.txt', 'wb') as f:
                    f.write(decrypted_data)
                
                # Verify contents
                print("\nVerifying contents...")
                with open(test_file_path, 'rb') as f:
                    original_content = f.read()
                with open('test_files/decrypted.txt', 'rb') as f:
                    decrypted_content = f.read()
                
                if original_content == decrypted_content:
                    print("✅ Success! Original and decrypted files match!")
                else:
                    print("❌ Error: Files don't match!")
            else:
                print(f"❌ Decryption failed: {response.json()}")
        else:
            print(f"❌ Encryption failed: {response.json()}")
        
        # Clean up
        print("\nCleaning up...")
        test_files = [
            'test_files/test.txt',
            'test_files/encrypted.bin',
            'test_files/keys.json',
            'test_files/decrypted.txt'
        ]
        for file in test_files:
            if os.path.exists(file):
                os.remove(file)
        print("Test files cleaned up")
        
    except Exception as e:
        print(f"❌ Error during testing: {str(e)}")

if __name__ == "__main__":
    test_api()