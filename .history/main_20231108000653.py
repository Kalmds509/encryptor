from cryptography.fernet import Fernet
from e import encrypt, decrypt

def main():
    user_key = input("Entrez votre clé secrète (laissez vide pour générer une nouvelle clé) : ").strip()
    
    if not user_key:
        key = Fernet.generate_key()[:10]  # Utilisez uniquement les 10 premiers caractères de la clé générée
    else:
        key = user_key[:10]  # Utilisez uniquement les 10 premiers caractères de la clé fournie par l'utilisateur
    
    text_to_encrypt = "Tèks Konfidansyèl"

    encrypted_text = encrypt(text_to_encrypt, key)
    print(f"Encrypted text: {encrypted_text}")

    decrypted_text = decrypt(encrypted_text, key)
    print(f"Decrypted text: {decrypted_text}")

if __name__ == "__main__":
    main()
