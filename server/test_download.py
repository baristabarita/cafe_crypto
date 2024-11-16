# test_downloads.py
import requests
import os
import json

def test_encryption_with_download():
    BASE_URL = 'http://localhost:5000/api'
    
    # Create test file
    test_file_path = 'test.txt'
    with open(test_file_path, 'w') as f:
        f.write("This is a test file for encryption and download!")
    
    try:
        # Test encryption
        print("Testing encryption and file download...")
        with open(test_file_path, 'rb') as f:
            files = {'file': ('test.txt', f)}
            response = requests.post(f'{BASE_URL}/encrypt', files=files)
        
        if response.status_code == 200:
            data = response.json()
            
            # Download encrypted file
            encrypted_url = f"http://localhost:5000{data['encrypted_file_url']}"
            keys_url = f"http://localhost:5000{data['keys_file_url']}"
            
            print("Downloading encrypted file...")
            encrypted_response = requests.get(encrypted_url)
            with open('downloaded_encrypted.bin', 'wb') as f:
                f.write(encrypted_response.content)
            
            print("Downloading keys file...")
            keys_response = requests.get(keys_url)
            with open('downloaded_keys.json', 'wb') as f:
                f.write(keys_response.content)
            
            # Test decryption with downloaded files
            print("\nTesting decryption with downloaded files...")
            with open('downloaded_encrypted.bin', 'rb') as ef, \
                 open('downloaded_keys.json', 'rb') as kf:
                files = {
                    'encrypted_file': ('encrypted.bin', ef),
                    'key_file': ('keys.json', kf)
                }
                response = requests.post(f'{BASE_URL}/decrypt', files=files)
            
            if response.status_code == 200:
                data = response.json()
                
                # Download decrypted file
                decrypted_url = f"http://localhost:5000{data['decrypted_file_url']}"
                print("Downloading decrypted file...")
                decrypted_response = requests.get(decrypted_url)
                with open('downloaded_decrypted.txt', 'wb') as f:
                    f.write(decrypted_response.content)
                
                # Verify contents
                print("\nVerifying contents...")
                with open(test_file_path, 'rb') as f:
                    original_content = f.read()
                with open('downloaded_decrypted.txt', 'rb') as f:
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
        files_to_clean = [
            test_file_path,
            'downloaded_encrypted.bin',
            'downloaded_keys.json',
            'downloaded_decrypted.txt'
        ]
        for file in files_to_clean:
            if os.path.exists(file):
                os.remove(file)
        
    except Exception as e:
        print(f"❌ Error during testing: {str(e)}")

if __name__ == "__main__":
    test_encryption_with_download()