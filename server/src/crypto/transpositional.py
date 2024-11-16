class TranspositionCipher:
    @staticmethod
    def encrypt(data: bytes, key: int) -> bytes:
        # Pad data if necessary
        padding = key - (len(data) % key) if len(data) % key != 0 else 0
        padded_data = data + bytes([padding] * padding)
        
        # Create matrix and transpose
        matrix = [padded_data[i:i+key] for i in range(0, len(padded_data), key)]
        transposed = bytes([matrix[row][col] for col in range(key) 
                          for row in range(len(matrix))])
        
        return bytes([padding]) + transposed
    
    @staticmethod
    def decrypt(data: bytes, key: int) -> bytes:
        padding = data[0]
        data = data[1:]
        
        rows = len(data) // key
        matrix = [data[i:i+rows] for i in range(0, len(data), rows)]
        
        original = bytes([matrix[col][row] for row in range(rows) 
                         for col in range(len(matrix))])
        
        return original[:-padding] if padding else original