# -ADVANCED-ENCRYPTION-TOOL #

 A TOOL TO ENCRYPT AND  DECRYPT FILES USING ADVANCED  ALGORITHMS LIKE AES-256 

 NAME : Konatham Chennakesavulu 
 
INTERN  ID:CT06DH1266 

 DOMAIN : CYBER SECURITY AND ETHICAL HACKING 

 DURATION : 6 WEEKS 

 MENTOR : NEELA SANTOSH 

## Overview
The **Advanced Encryption Tool** is a robust Python-based application designed to encrypt and decrypt files securely using **AES-256 encryption**. This tool ensures data confidentiality by providing a user-friendly interface for protecting sensitive information.

## Features
- **AES-256 Encryption**: Uses the industry-standard **Advanced Encryption Standard (AES)** with a **256-bit key**.
- **Secure Random Key Generation**: Generates cryptographic keys using a secure random function.
- **File Encryption & Decryption**: Encrypts and decrypts files efficiently while preserving data integrity.
- **User-Friendly Interface**: Simple command-line interface (CLI) for ease of use.
- **Cross-Platform**: Works on Windows, Linux, and macOS.

## How It Works
1. The user chooses to encrypt or decrypt a file.
2. **Encryption**: The tool generates a random **256-bit key**, encrypts the file with AES-256 in **CBC mode**, and writes the encrypted data along with the IV (Initialization Vector) to an output file.
3. **Decryption**: Reads the IV from the encrypted file, decrypts the content using the provided key, and saves the original file.

## Installation
### Prerequisites
- Python 3.x installed
- Install required libraries using:
  ```bash
  pip install pycryptodome
  ```

### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/advanced-encryption-tool.git
   cd advanced-encryption-tool
   ```
2. Run the script:
   ```bash
   python advanced_encryption_tool.py
   ```

## Usage
### Encrypt a File
```plaintext
Do you want to (E)ncrypt or (D)ecrypt? e
Enter the file path: secret.txt
Enter the output file path: encrypted.dat
```
#### Output:
```plaintext
File encrypted successfully: encrypted.dat
```

### Decrypt a File
```plaintext
Do you want to (E)ncrypt or (D)ecrypt? d
Enter the file path: encrypted.dat
Enter the output file path: decrypted.txt
```
#### Example Output:
```plaintext
File decrypted successfully: decrypted.txt
```

## Customization
- Modify `AES.MODE_CBC` to **GCM mode** for authenticated encryption.
- Store or input keys securely instead of generating new ones every time.
- Extend functionality to **encrypt/decrypt text messages** or integrate **password-based encryption**.

## Security Notes
- **Key Management**: Ensure that encryption keys are stored securely and not hardcoded.
- **IV Handling**: The IV is randomly generated for each encryption and stored with the ciphertext.
- **Padding Scheme**: Uses space padding; can be modified to **PKCS7 padding**.

## Legal Disclaimer
This tool is intended for legal and ethical use only. Unauthorized encryption or decryption of files may violate data privacy laws.




