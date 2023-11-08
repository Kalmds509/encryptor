# Nan encryptor/example.py

from encryptor.encryptor import encrypt_aes, decrypt

text = "Tèks Konfidansyèl"
key = "kle_sekre_a"

# Test ak algorit AES
encrypted_text_aes = encrypt(text, key, algorithm='aes')
decrypted_text_aes = decrypt(encrypted_text_aes, key, algorithm='aes')

print("AES Encryption:")
print(f"Original Text: {text}")
print(f"Encrypted Text: {encrypted_text_aes}")
print(f"Decrypted Text: {decrypted_text_aes}")
print("\n")

# Test ak algorit RSA
private_key = get_private_key()
public_key = private_key.public_key()

encrypted_text_rsa = encrypt(text, key, algorithm='rsa')
decrypted_text_rsa = decrypt(encrypted_text_rsa, key, algorithm='rsa')

print("RSA Encryption:")
print(f"Original Text: {text}")
print(f"Encrypted Text: {encrypted_text_rsa}")
print(f"Decrypted Text: {decrypted_text_rsa}")
