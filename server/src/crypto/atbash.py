# server/crypto/atbash.py
def atbash_encrypt(content):
    """Encrypt the given file content using the Atbash cipher."""
    # Create the mapping for Atbash cipher
    atbash_map = {chr(i): chr(90 - (i - 65)) for i in range(65, 91)}
    atbash_map.update({chr(i): chr(122 - (i - 97)) for i in range(97, 123)})
    
    # Encrypt the input content using Atbash mapping
    encrypted_content = ''.join(atbash_map.get(char, char) for char in content)
    return encrypted_content

def atbash_decrypt(content):
    """Decrypt the given file content using the Atbash cipher."""
    return atbash_encrypt(content)