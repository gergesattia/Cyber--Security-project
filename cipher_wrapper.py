"""
Cipher Wrapper Module - Provides standardized interface for all ciphers using core_ciphers
"""

import core_ciphers

class CipherManager:
    """Unified interface for all encryption algorithms"""
    
    @staticmethod
    def caesar_encrypt(text, key):
        try:
            shift = int(key)
            return core_ciphers.caesar_encrypt(text, shift)
        except Exception as e:
            raise ValueError(f"Caesar encryption error: {str(e)}")
    
    @staticmethod
    def caesar_decrypt(text, key):
        try:
            shift = int(key)
            return core_ciphers.caesar_decrypt(text, shift)
        except Exception as e:
            raise ValueError(f"Caesar decryption error: {str(e)}")
    
    @staticmethod
    def vigenere_encrypt(text, key):
        try:
            return core_ciphers.vigenere_encrypt(text, key)
        except Exception as e:
            raise ValueError(f"Vigenere encryption error: {str(e)}")
    
    @staticmethod
    def vigenere_decrypt(text, key):
        try:
            return core_ciphers.vigenere_decrypt(text, key)
        except Exception as e:
            raise ValueError(f"Vigenere decryption error: {str(e)}")
    
    @staticmethod
    def playfair_encrypt(text, key):
        try:
            matrix = core_ciphers.create_matrix(key)
            return core_ciphers.playfair_encrypt(text, matrix)
        except Exception as e:
            raise ValueError(f"Playfair encryption error: {str(e)}")
    
    @staticmethod
    def playfair_decrypt(text, key):
        try:
            matrix = core_ciphers.create_matrix(key)
            return core_ciphers.playfair_decrypt(text, matrix)
        except Exception as e:
            raise ValueError(f"Playfair decryption error: {str(e)}")
    
    @staticmethod
    def rot13_encrypt(text, key=None):
        try:
            return core_ciphers.rot13(text)
        except Exception as e:
            raise ValueError(f"ROT13 encryption error: {str(e)}")
    
    @staticmethod
    def rot13_decrypt(text, key=None):
        try:
            return core_ciphers.rot13(text)
        except Exception as e:
            raise ValueError(f"ROT13 decryption error: {str(e)}")
    
    @staticmethod
    def railfence_encrypt(text, key):
        try:
            rails = int(key)
            return core_ciphers.rail_encrypt(text, rails)
        except Exception as e:
            raise ValueError(f"Rail Fence encryption error: {str(e)}")
    
    @staticmethod
    def railfence_decrypt(text, key):
        try:
            rails = int(key)
            return core_ciphers.rail_decrypt(text, rails)
        except Exception as e:
            raise ValueError(f"Rail Fence decryption error: {str(e)}")
    
    @staticmethod
    def transposition_encrypt(text, key):
        try:
            return core_ciphers.col_encrypt(text, key)
        except Exception as e:
            raise ValueError(f"Transposition encryption error: {str(e)}")
    
    @staticmethod
    def transposition_decrypt(text, key):
        try:
            return core_ciphers.col_decrypt(text, key)
        except Exception as e:
            raise ValueError(f"Transposition decryption error: {str(e)}")
            
    @staticmethod
    def hill_encrypt(text, key):
        try:
            parts = key.split(',')
            if len(parts) != 4:
                raise ValueError("Key must be 4 numbers separated by commas (e.g. 5,17,8,3)")
            matrix = [
                [int(parts[0]), int(parts[1])],
                [int(parts[2]), int(parts[3])]
            ]
            return core_ciphers.hill_encrypt(text, matrix)
        except ValueError as ve:
            raise ve
        except Exception as e:
            raise ValueError(f"Hill encryption error: {str(e)}")
            
    @staticmethod
    def hill_decrypt(text, key):
        try:
            parts = key.split(',')
            if len(parts) != 4:
                raise ValueError("Key must be 4 numbers separated by commas (e.g. 5,17,8,3)")
            matrix = [
                [int(parts[0]), int(parts[1])],
                [int(parts[2]), int(parts[3])]
            ]
            return core_ciphers.hill_decrypt(text, matrix)
        except ValueError as ve:
            raise ve
        except Exception as e:
            raise ValueError(f"Hill decryption error: {str(e)}")


# Dictionary mapping cipher names to their functions
CIPHERS = {
    "Caesar Cipher": {
        "encrypt": CipherManager.caesar_encrypt,
        "decrypt": CipherManager.caesar_decrypt,
        "key_type": "integer (shift value)",
        "example_key": "3"
    },
    "Vigenere Cipher": {
        "encrypt": CipherManager.vigenere_encrypt,
        "decrypt": CipherManager.vigenere_decrypt,
        "key_type": "string (keyword)",
        "example_key": "KEY"
    },
    "Playfair Cipher": {
        "encrypt": CipherManager.playfair_encrypt,
        "decrypt": CipherManager.playfair_decrypt,
        "key_type": "string (keyword)",
        "example_key": "PLAYFAIR"
    },
    "ROT13 Cipher": {
        "encrypt": CipherManager.rot13_encrypt,
        "decrypt": CipherManager.rot13_decrypt,
        "key_type": "none (no key needed)",
        "example_key": "N/A"
    },
    "Rail Fence Cipher": {
        "encrypt": CipherManager.railfence_encrypt,
        "decrypt": CipherManager.railfence_decrypt,
        "key_type": "integer (number of rails)",
        "example_key": "3"
    },
    "Transposition Cipher": {
        "encrypt": CipherManager.transposition_encrypt,
        "decrypt": CipherManager.transposition_decrypt,
        "key_type": "string (keyword for column ordering)",
        "example_key": "KEY"
    },
    "Hill Cipher": {
        "encrypt": CipherManager.hill_encrypt,
        "decrypt": CipherManager.hill_decrypt,
        "key_type": "4 numbers separated by commas",
        "example_key": "5,17,8,3"
    }
}
