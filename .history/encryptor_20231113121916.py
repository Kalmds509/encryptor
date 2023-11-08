# Dans encryptor/encryption.py

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def generate_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        salt=salt,
        iterations=100000,
        length=32,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())
    return key

def encrypt_aes(text, key):
    cipher = Cipher(algorithms.AES(key), modes.CFB, backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_text = encryptor.update(text.encode()) + encryptor.finalize()
    return encrypted_text

def decrypt_aes(encrypted_text, key):
    cipher = Cipher(algorithms.AES(key), modes.CFB, backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_text = decryptor.update(encrypted_text) + decryptor.finalize()
    return decrypted_text.decode()

def encrypt_rsa(text, public_key):
    ciphertext = public_key.encrypt(
        text.encode(),
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
    )
    return ciphertext

def decrypt_rsa(encrypted_text, private_key):
    plaintext = private_key.decrypt(
        encrypted_text,
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
    )
    return plaintext.decode()

def encrypt(text, key, algorithm='aes'):
    salt = b'salt_value_here'
    generated_key = generate_key(key, salt)

    if algorithm == 'aes':
        return encrypt_aes(text, generated_key)
    elif algorithm == 'rsa':
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        return encrypt_rsa(text, private_key.public_key())
    else:
        raise ValueError("Algorithme non pris en charge")

def decrypt(encrypted_text, key, algorithm='aes'):
    salt = b'salt_value_here'
    generated_key = generate_key(key, salt)

    if algorithm == 'aes':
        return decrypt_aes(encrypted_text, generated_key)
    elif algorithm == 'rsa':
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        return decrypt_rsa(encrypted_text, private_key)
    else:
        raise ValueError("Algorithme non pris en charge")
