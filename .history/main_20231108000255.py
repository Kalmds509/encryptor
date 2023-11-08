from cryptography.fernet import Fernet
from encryption import encrypt, decrypt
from base64 import urlsafe_b64decode

def main():
    user_key = input("Entrez votre clé secrète (laissez vide pour générer une nouvelle clé) : ").strip()
    
    if not user_key:
        key = Fernet.generate_key()
    else:
        try:
            key = urlsafe_b64decode(user_key)
        except ValueError:
            print("Erreur : la clé fournie n'est pas valide.")
            return
    
    text_to_encrypt = "Tèks Konfidansyèl"

    encrypted_text = encrypt(text_to_encrypt, key)
    print(f"Encrypted text: {encrypted_text}")

    decrypted_text = decrypt(encrypted_text, key)
    print(f"Decrypted text: {decrypted_text}")

if __name__ == "__main__":
    main()
