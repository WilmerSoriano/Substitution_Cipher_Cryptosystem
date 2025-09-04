"""
Simple Abstraction of code:
    1st Ask user for filename, txt file, return the result to file.
    2nd Using the key, shift the letters
    2nd Determine the encrypt and decrypt
        - if encrypt
            - match the text with key mapping
            - return and save to file
        - if decrypt
            - reverse the key mapping
            - return and reveal message
    3rd save the message and print
"""

import string

alphabet = list(string.ascii_lowercase)

def shift_letter(key):
    shift_alpha = [""] * 26
    for i in range(len(alphabet)):
        shift_alpha[(i+key) % 26] = alphabet[i]

    return dict(zip(alphabet, shift_alpha)) # Now alphabet are mapped to respective shifted letter.

# Changes the phrase into a substitution cipher
def encrpyt(text, key_word):
    encrpyt_word = ""

    for letter in text:
        if letter in key_word:
            encrpyt_word += key_word[letter]
        else:
            encrpyt_word += letter # Not a alphabet, must be space or a character

    encrpyt_word = "scc_"+encrpyt_word
    print("Encrypted: "+ encrpyt_word)

    return encrpyt_word

def decrpyt(text, key_word):
    decrpyt_word = ""
    reverse_key = {v: k for k, v in key_word.items()} # Reverse the mapping (e.g if A|x then x|A)

    for letter in text:
        if letter in reverse_key:
            decrpyt_word += reverse_key[letter]
        else:
            decrpyt_word += letter
    print("Decrpyted word: "+decrpyt_word)
    return decrpyt_word

# Take user input and handle the file
def handleFile(filename, key):
    text = ""
    with open(filename, 'r') as file:
        text = file.read()
    # scc or substitution cipher cryptosystem is how am going to identify decryption is needed
    if "scc_" in text:
        text = text.replace("scc_", "")
        text = decrpyt(text,key)
    else:
        text = encrpyt(text,key)
    
    print("saved to file!")
    with open(filename, 'w') as file:
        file.write(text)


if __name__ == '__main__':
    print("="*24)
    filename = input("Please enter a filename: ")
    key = input("Please enter the key: ")
    print("="*24)

    shifted = shift_letter(int(key))

    handleFile(filename,shifted)

