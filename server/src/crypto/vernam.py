import os

class VernamCipher:
    @staticmethod
    def generate_key(length: int) -> bytes:
        return os.urandom(length)
    
    @staticmethod
    def encrypt(data: bytes, key: bytes = None) -> tuple[bytes, bytes]:
        if key is None:
            key = VernamCipher.generate_key(len(data))
        encrypted = bytes([data[i] ^ key[i] for i in range(len(data))])
        return encrypted, key
    
    @staticmethod
    def decrypt(data: bytes, key: bytes) -> bytes:
        return bytes([data[i] ^ key[i] for i in range(len(data))])