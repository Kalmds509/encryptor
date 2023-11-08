from cryptography.fernet import Fernet
from encryption import encrypt, decrypt

# Mot de passe par défaut
DEFAULT_PASSWORD = "mon_password_secret"

def main():
    # Génération de la clé à partir du mot de passe par défaut
    key = Fernet.generate_key()
    
    # Vérification du mot de passe
    entered_password = input("Entrez le mot de passe : ")
    if entered_password != DEFAULT_PASSWORD:
        print("Mot de passe incorrect. L'encryption et le déchiffrement ne sont pas autorisés.")
        return

    # Le mot de passe est correct, poursuivre avec l'encryption/déchiffrement
    text_to_decrip = input("Entrez le texte à chiffrer : ")

    # encrypted_text = encrypt(text_to_encrypt, key)
    # print(f"Encrypted text: {encrypted_text}")

    decrypted_text = decrypt(text_to_decrip, key)
    print(f"Decrypted text: {decrypted_text}")

if __name__ == "__main__":
    main()
