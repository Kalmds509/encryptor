from cryptography.fernet import Fernet
from encryption import encrypt, decrypt

def main():
    user_key = input("Entrez votre clé secrète : ")
    key = Fernet.generate_key() if not user_key else user_key.encode()
    
    text_to_encrypt = "Tèks Konfidansyèl"

    encrypted_text = encrypt(text_to_encrypt, key)
    print(f"Encrypted text: {encrypted_text}")

    decrypted_text = decrypt(encrypted_text, key)
    print(f"Decrypted text: {decrypted_text}")

if __name__ == "__main__":
    main()
