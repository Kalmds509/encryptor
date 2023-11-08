# Nan encryptor/example.py

from encryptor import encrypt_aes, decrypt_aes, encrypt_rsa, decrypt_rsa,generate_key,get_private_key

def main():
    text = "Tèks Konfidansyèl"
    key = "kle_sekre_a"

    # Test ak algorit AES
    key_aes = generate_key(key)
    encrypted_text_aes = encrypt_aes(text, key_aes)
    decrypted_text_aes = decrypt_aes(encrypted_text_aes, key_aes)

    print("AES Encryption:")
    print(f"Original Text: {text}")
    print(f"Encrypted Text: {encrypted_text_aes}")
    print(f"Decrypted Text: {decrypted_text_aes}")
    print("\n")

    # Test ak algorit RSA
    private_key = get_private_key()
    public_key = private_key.public_key()

    encrypted_text_rsa = encrypt_rsa(text, public_key)
    decrypted_text_rsa = decrypt_rsa(encrypted_text_rsa, private_key)

    print("RSA Encryption:")
    print(f"Original Text: {text}")
    print(f"Encrypted Text: {encrypted_text_rsa}")
    print(f"Decrypted Text: {decrypted_text_rsa}")

if __name__ == "__main__":
    main()
