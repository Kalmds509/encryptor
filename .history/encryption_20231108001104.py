from cryptography.fernet import Fernet
from base64 import urlsafe_b64encode, urlsafe_b64decode

def encrypt(text, key):
    fernet = Fernet(key)
    encrypted_text = fernet.encrypt(text.encode())
    return urlsafe_b64encode(encrypted_text)

def decrypt(encrypted_text, key):
    fernet = Fernet(key)
    decrypted_text = fernet.decrypt(urlsafe_b64decode(encrypted_text)).decode('utf-8')
    return decrypted_text
