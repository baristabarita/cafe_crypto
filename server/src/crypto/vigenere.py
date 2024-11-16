class VigenereCipher:
    @staticmethod
    def encrypt(data: bytes, key: bytes) -> bytes:
        return bytes([(data[i] + key[i % len(key)]) % 256 
                     for i in range(len(data))])
    
    @staticmethod
    def decrypt(data: bytes, key: bytes) -> bytes:
        return bytes([(data[i] - key[i % len(key)]) % 256 
                     for i in range(len(data))])
