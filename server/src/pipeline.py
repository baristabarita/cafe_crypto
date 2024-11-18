# pipeline.py
from src.crypto.caesar import CaesarCipher
from src.crypto.transpositional import TranspositionCipher
from src.crypto.vigenere import VigenereCipher
from src.crypto.vernam import VernamCipher
from src.crypto.rsa import RSACipher
from src.utils.file_handler import FileHandler
import json
import os

class CryptoPipeline:
    def __init__(self):
        self.file_handler = FileHandler()
        self.caesar = CaesarCipher()
        self.transposition = TranspositionCipher()
        self.vigenere = VigenereCipher()
        self.vernam = VernamCipher()
        self.rsa = RSACipher()
        
        # Generate RSA keys
        self.rsa.generate_keys()
    
    def encrypt_file(self, input_path: str) -> tuple[str, str]:
        """
        Encrypt file using all algorithms in sequence.
        Returns tuple of (encrypted_file_path, key_file_path)
        """
        # Read file
        data = self.file_handler.read_file(input_path)
        
        # Apply encryption algorithms in sequence
        # 1. Caesar Cipher
        caesar_shift = 13
        data = self.caesar.encrypt(data, caesar_shift)
        
        # 2. Transposition
        trans_key = 8 
        data = self.transposition.encrypt(data, trans_key)
        
        # 3. Vigenere
        vigenere_key = b"SECRETKEY"
        data = self.vigenere.encrypt(data, vigenere_key)
        
        # 4. Vernam
        data, vernam_key = self.vernam.encrypt(data)
        
        # 5. RSA
        data = self.rsa.encrypt(data)
        
        # Save encrypted file
        encrypted_path = self.file_handler.create_output_path(input_path, "encrypted")
        self.file_handler.write_file(encrypted_path, data)
        
        # Save encryption keys
        keys = {
            "caesar_shift": caesar_shift,
            "trans_key": trans_key,
            "vigenere_key": self.file_handler.bytes_to_base64(vigenere_key),
            "vernam_key": self.file_handler.bytes_to_base64(vernam_key),
            "original_extension": self.file_handler.get_file_extension(input_path)
        }
        
        key_path = self.file_handler.create_output_path(input_path, "keys.json")
        with open(key_path, 'w') as f:
            json.dump(keys, f)
        
        return encrypted_path, key_path
    
    def decrypt_file(self, encrypted_path: str, key_path: str) -> str:
        """
        Decrypt file using all algorithms in reverse sequence.
        Returns decrypted file path.
        """
        # Load keys
        with open(key_path, 'r') as f:
            keys = json.load(f)
        
        # Read encrypted data
        data = self.file_handler.read_file(encrypted_path)
        
        # Apply decryption algorithms in reverse sequence
        # 5. RSA
        data = self.rsa.decrypt(data)
        
        # 4. Vernam
        vernam_key = self.file_handler.base64_to_bytes(keys["vernam_key"])
        data = self.vernam.decrypt(data, vernam_key)
        
        # 3. Vigenere
        vigenere_key = self.file_handler.base64_to_bytes(keys["vigenere_key"])
        data = self.vigenere.decrypt(data, vigenere_key)
        
        # 2. Transposition
        data = self.transposition.decrypt(data, keys["trans_key"])
        
        # 1. Caesar Cipher
        data = self.caesar.decrypt(data, keys["caesar_shift"])
        
        # Save decrypted file
        decrypted_path = self.file_handler.create_output_path(
            encrypted_path.replace("_encrypted", ""), 
            "decrypted" + keys["original_extension"]
        )
        self.file_handler.write_file(decrypted_path, data)
        
        return decrypted_path