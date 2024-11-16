# crypto/rsa.py
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES 
import base64

class RSACipher:
    def __init__(self, key_size=2048):
        self.key_size = key_size
        self.key = None
        self.public_key = None
        self.private_key = None
    
    def generate_keys(self):
        self.key = RSA.generate(self.key_size)
        self.public_key = self.key.publickey()
        self.private_key = self.key
        return (self.public_key, self.private_key)
    
    def encrypt(self, data: bytes) -> bytes:
        # Use hybrid encryption due to RSA size limitations
        session_key = get_random_bytes(16)
        cipher_rsa = PKCS1_OAEP.new(self.public_key)
        enc_session_key = cipher_rsa.encrypt(session_key)
        
        # Encrypt data with session key
        cipher_aes = AES.new(session_key, AES.MODE_EAX)
        ciphertext, tag = cipher_aes.encrypt_and_digest(data)
        
        return base64.b64encode(enc_session_key + cipher_aes.nonce + tag + ciphertext)
    
    def decrypt(self, data: bytes) -> bytes:
        data = base64.b64decode(data)
        enc_session_key = data[:self.private_key.size_in_bytes()]
        nonce = data[self.private_key.size_in_bytes():self.private_key.size_in_bytes()+16]
        tag = data[self.private_key.size_in_bytes()+16:self.private_key.size_in_bytes()+32]
        ciphertext = data[self.private_key.size_in_bytes()+32:]
        
        # Decrypt session key
        cipher_rsa = PKCS1_OAEP.new(self.private_key)
        session_key = cipher_rsa.decrypt(enc_session_key)
        
        # Decrypt data
        cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
        data = cipher_aes.decrypt_and_verify(ciphertext, tag)
        return data