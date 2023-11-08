# Dans votre code principal (main.py)

from encryptor import encrypt, decrypt

text = "Tèks Konfidansyèl"
key = "kle_sekre_a"

# Choisir l'algorithme (aes ou rsa)
algorithm = 'aes'

# encrypted_text = encrypt(text, key, algorithm=algorithm)
# decrypted_text = decrypt(encrypted_text, key, algorithm=algorithm)

print(f"Original Text: {text}")
print(f"Encrypted Text: {encrypted_text}")
print(f"Decrypted Text: {decrypted_text}")
