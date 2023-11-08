from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from base64 import urlsafe_b64encode, urlsafe_b64decode
import os

def pad(data):
    block_size = algorithms.AES.block_size // 8
    padding_length = block_size - (len(data) % block_size)
    padding = bytes([padding_length] * padding_length)
    return data + padding

def unpad(data):
    padding_length = data[-1]
    return data[:-padding_length]

def encrypt(text, key):
key = urlsafe_b64encode(os.urandom(32)).decode('utf-8')

    text = text.encode('utf-8')
    text = pad(text)

    iv = os.urandom(algorithms.AES.block_size // 8)

    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(text) + encryptor.finalize()

    return urlsafe_b64encode(iv + ciphertext)

def decrypt(encrypted_text, key):
    key = urlsafe_b64decode(key)
    encrypted_text = urlsafe_b64decode(encrypted_text)

    iv = encrypted_text[:algorithms.AES.block_size // 8]
    ciphertext = encrypted_text[algorithms.AES.block_size // 8:]

    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_text = decryptor.update(ciphertext) + decryptor.finalize()

    return unpad(decrypted_text).decode('utf-8')
