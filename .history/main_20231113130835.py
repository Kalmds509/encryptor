from e import encrypt, decrypt

def main():
    key = "klye_sekre_a"
    text_to_encrypt = "Tèks Konfidansyèl"

    encrypted_text = encrypt(text_to_encrypt, key)
    print(f"Encrypted text: {encrypted_text}")

    decrypted_text = decrypt(encrypted_text, key)
    print(f"Decrypted text: {decrypted_text}")

if __name__ == "__main__":
    main()
