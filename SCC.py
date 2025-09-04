"""
Simple Abstraction of code:
    1st handle the txt file / ask user for file
    2nd determine the encry/decry
        - if encrypt
            - take the message
            - make a key
            - hide the message
        - if decrypt
            - take the message
            - use the key
            - reveal message
    3rd save the message and print in txt file
"""

import time
import string

alphabet = list(string.ascii_lowercase)

def shift_letter(key):
    shift_alpha = [""] * 26
    for i in range(len(alphabet)):
        shift_alpha[(i+key) % 26] = alphabet[i]

    return dict(zip(alphabet, shift_alpha)) # Now alphabet are mapped to respective shifted letter.

# Changes the phrase into sub-cipher and keeps space or numbers
def encrpyt(text, key_word):
    encrpyt_word = ""

    for letter in text:
        if letter in key_word:
            encrpyt_word += key_word[letter]
        else:
            encrpyt_word += letter

    encrpyt_word = "scc_"+encrpyt_word
    print("Encrypted: "+ encrpyt_word)

    return encrpyt_word

def decrpyt(text, key_word):
    decrpyt_word = ""
    reverse_key = {v: k for k, v in key_word.items()}

    for letter in text:
        if letter in reverse_key:
            decrpyt_word += reverse_key[letter]
        else:
            decrpyt_word += letter

# 1st. Take user input and handle the file
def handleFile(filename, key):
    text = ""
    with open(filename, 'r') as file:
        text = file.read()

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

