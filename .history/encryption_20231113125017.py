from cryptography.fernet import Fernet

def encrypt(text, key):
    cipher_suite = Fernet(key)
    encrypted_text = cipher_suite.encrypt(text.encode())
    return encrypted_text

def decrypt(encrypted_text, key):
    cipher_suite = Fernet(key)
    decrypted_text = cipher_suite.decrypt(encrypted_text).decode()
    return decrypted_text

# Example usage:
key = Fernet.generate_key()  # Generate a random key
text_to_encrypt = "Tèks Konfidansyèl"

encrypted_text = encrypt(text_to_encrypt, key)
print(f"Encrypted text: {encrypted_text}")

decrypted_text = decrypt(encrypted_text, key)
print(f"Decrypted text: {decrypted_text}")
