# utils/file_handler.py
import os
import base64

class FileHandler:
    @staticmethod
    def read_file(file_path):
        """Read file and return bytes"""
        with open(file_path, 'rb') as file:
            return file.read()
    
    @staticmethod
    def write_file(file_path, data):
        """Write bytes to file"""
        with open(file_path, 'wb') as file:
            file.write(data)
    
    @staticmethod
    def bytes_to_base64(data):
        """Convert bytes to base64 string"""
        return base64.b64encode(data).decode('utf-8')
    
    @staticmethod
    def base64_to_bytes(data):
        """Convert base64 string to bytes"""
        return base64.b64decode(data.encode('utf-8'))

    @staticmethod
    def get_file_extension(file_path):
        """Get file extension from path"""
        return os.path.splitext(file_path)[1]
    
    @staticmethod
    def create_output_path(original_path, suffix):
        """Create output path with suffix"""
        base, ext = os.path.splitext(original_path)
        return f"{base}_{suffix}{ext}"