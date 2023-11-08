from cryptography.fernet import Fernet
from encryption import encrypt, decrypt

def main():
    key = Fernet.generate_key()
    
    text_to_encrypt = input("Entrez le texte à chiffrer : ")

    encrypted_text = encrypt(text_to_encrypt, key)
    print(f"Encrypted text: {encrypted_text}")

    decrypted_text = decrypt(encrypted_text, key)
    print(f"Decrypted text: {decrypted_text}")

if __name__ == "__main__":
    main()
