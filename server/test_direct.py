import os
from src.pipeline import CryptoPipeline

def test_encryption_decryption():
    # Create test files directory if it doesn't exist
    if not os.path.exists('test_files'):
        os.makedirs('test_files')
    
    # Create a test file with some content
    test_file_path = 'test_files/test_text.txt'
    with open(test_file_path, 'wb') as f:
        f.write(b"This is a test file with some content!\nMultiple lines!\n123456789")
    
    print(f"Created test file: {test_file_path}")
    
    # Initialize the pipeline
    pipeline = CryptoPipeline()
    
    try:
        # Encrypt the file
        print("\nEncrypting file...")
        encrypted_path, key_path = pipeline.encrypt_file(test_file_path)
        print(f"Encrypted file saved to: {encrypted_path}")
        print(f"Keys saved to: {key_path}")
        
        # Decrypt the file
        print("\nDecrypting file...")
        decrypted_path = pipeline.decrypt_file(encrypted_path, key_path)
        print(f"Decrypted file saved to: {decrypted_path}")
        
        # Verify the contents
        print("\nVerifying contents...")
        with open(test_file_path, 'rb') as f:
            original_content = f.read()
        with open(decrypted_path, 'rb') as f:
            decrypted_content = f.read()
        
        if original_content == decrypted_content:
            print("✅ Success! Original and decrypted files match!")
        else:
            print("❌ Error: Files don't match!")
            
        # Clean up
        print("\nCleaning up...")
        os.remove(encrypted_path)
        os.remove(key_path)
        os.remove(decrypted_path)
        os.remove(test_file_path)
        print("Test files cleaned up")
        
    except Exception as e:
        print(f"❌ Error during testing: {str(e)}")

if __name__ == "__main__":
    test_encryption_decryption()