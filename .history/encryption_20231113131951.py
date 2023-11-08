from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from base64 import urlsafe_b64encode, urlsafe_b64decode
import os

def generate_rsa_key_pair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key

def save_key_to_file(key, filename):
    with open(filename, 'wb') as key_file:
        key_file.write(key)

def load_key_from_file(filename, key_type):
    with open(filename, 'rb') as key_file:
        key_data = key_file.read()
        if key_type == 'private':
            key = serialization.load_pem_private_key(
                key_data,
                password=None,
                backend=default_backend()
            )
        elif key_type == 'public':
            key = serialization.load_pem_public_key(
                key_data,
                backend=default_backend()
            )
        else:
            raise ValueError("Invalid key type")
        return key

def generate_aes_key():
    return urlsafe_b64encode(os.urandom(algorithms.AES.block_size // 8)).decode('utf-8')

def encrypt_aes(text, key):
    key = urlsafe_b64decode(key)
    text = text.encode('utf-8')
    text = pad(text)

    iv = os.urandom(algorithms.AES.block_size // 8)

    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(text) + encryptor.finalize()

    return urlsafe_b64encode(iv + ciphertext)

def decrypt_aes(encrypted_text, key):
    key = urlsafe_b64decode(key)
    encrypted_text = urlsafe_b64decode(encrypted_text)

    iv = encrypted_text[:algorithms.AES.block_size // 8]
    ciphertext = encrypted_text[algorithms.AES.block_size // 8:]

    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_text = decryptor.update(ciphertext) + decryptor.finalize()

    return unpad(decrypted_text).decode('utf-8')

def encrypt_rsa(text, public_key):
    ciphertext = public_key.encrypt(
        text.encode('utf-8'),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return ciphertext

def decrypt_rsa(ciphertext, private_key):
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return plaintext.decode('utf-8')

def pad(data):
    block_size = algorithms.AES.block_size // 8
    padding_length = block_size - (len(data) % block_size)
    padding = bytes([padding_length] * padding_length)
    return data + padding

def unpad(data):
    padding_length = data[-1]
    return data[:-padding_length]

# Jenere yon pè piblik ak yon kle prive RSA
private_key_rsa, public_key_rsa = generate_rsa_key_pair()

# Jenere yon kle AES
aes_key = generate_aes_key()

# Enkripte tèks la avèk kle RSA piblik la
text_to_encrypt = "Tèks Konfidansyèl"
encrypted_text_rsa = encrypt_rsa(text_to_encrypt, public_key_rsa)
print(f"Encrypted text with RSA: {encrypted_text_rsa}")

# Enkripte tèks la avèk kle AES
encrypted_text_aes = encrypt_aes(text_to_encrypt, aes_key)
print(f"Encrypted text with AES: {encrypted_text_aes}")

# Dekripte tèks la avèk kle RSA prive a
decrypted_text_rsa = decrypt_rsa(encrypted_text_rsa, private_key_rsa)
print(f"Decrypted text with RSA: {decrypted_text_rsa}")

# Dekripte tèks la avèk kle AES
decrypted_text_aes = decrypt_aes(encrypted_text_aes, aes_key)
print(f"Decrypted text with AES: {decrypted_text_aes}")
