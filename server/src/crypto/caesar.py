class CaesarCipher:
    @staticmethod
    def encrypt(data: bytes, shift: int) -> bytes:
        return bytes([(b + shift) % 256 for b in data])
    
    @staticmethod
    def decrypt(data: bytes, shift: int) -> bytes:
        return bytes([(b - shift) % 256 for b in data])