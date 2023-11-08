# Dans votre code principal (main.py)

from encryptor import encrypt, decrypt

text = "Tèks Konfidansyèl"
key = "kle_sekre_a"

# Choisir l'algorithme (aes ou rsa)
algorithm = 'aes'

encrypted_text = encrypt(text, key, algo=algorithm)  # Modifier 'algorithm' à 'algo'
decrypted_text = decrypt(encrypted_text, key, algo=algorithm)  # Modifier 'algorithm' à 'algo'

print(f"Original Text: {text}")
print(f"Encrypted Text: {encrypted_text}")
print(f"Decrypted Text: {decrypted_text}")
