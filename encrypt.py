from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os
import base64

def pad(data):
    """Pad data to make it a multiple of AES block size."""
    return data + b" " * (AES.block_size - len(data) % AES.block_size)

def encrypt_file(input_file, output_file, key):
    """Encrypt a file using AES-256."""
    cipher = AES.new(key, AES.MODE_CBC, get_random_bytes(16))
    
    with open(input_file, 'rb') as f:
        plaintext = f.read()
    
    ciphertext = cipher.encrypt(pad(plaintext))
    
    with open(output_file, 'wb') as f:
        f.write(cipher.iv + ciphertext)
    print(f"File encrypted successfully: {output_file}")

def decrypt_file(input_file, output_file, key):
    """Decrypt a file using AES-256."""
    with open(input_file, 'rb') as f:
        iv = f.read(16)
        ciphertext = f.read()
    
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext).rstrip(b" ")
    
    with open(output_file, 'wb') as f:
        f.write(plaintext)
    print(f"File decrypted successfully: {output_file}")

def main():
    key = get_random_bytes(32)  # AES-256 key
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().lower()
    input_file = input("Enter the file path: ")
    output_file = input("Enter the output file path: ")
    
    if choice == 'e':
        encrypt_file(input_file, output_file, key)
    elif choice == 'd':
        decrypt_file(input_file, output_file, key)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
