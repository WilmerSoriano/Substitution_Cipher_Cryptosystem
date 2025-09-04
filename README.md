# Substitution_Cipher_Cryptosystem
* Show casing my understanding of Substitution cipher and cryptosystem.
* (NOTE: DO NOT USE FOR REAL LIFE ENCRYPTION/DECRYPTION ... don't use it for anything important)
---

This project is a **simple encryption and decryption tool** using a substitution cipher.  
It allows you to encrypt or decrypt text stored in a `.txt` file by shifting letters in the alphabet with a user-provided key.

---

## How It Works
1. **Shift Mapping**:  
   A key (integer) is used to shift the alphabet. For example, with a key of `2`, `a → c`, `b → d`, etc.
2. **Encryption**:  
   - Plain text is converted using the shifted mapping.
   - The encrypted output is prefixed with `scc_` to mark it as encrypted.
3. **Decryption**:  
   - If the file contains text starting with `scc_`, the program reverses the mapping to recover the original message.
4. **File Handling**:  
   - The program reads the given text file, applies encryption or decryption, and overwrites the file with the result.

---

## Requirements
- Python 3.x

No external libraries are required.

---

## Usage
1. Create a text file (a `example.txt` is provided) with the content you want to encrypt or decrypt.
2. Run the script:
   ```bash
   python SCC.py
   ```
3. Follow the instructions on the program.
