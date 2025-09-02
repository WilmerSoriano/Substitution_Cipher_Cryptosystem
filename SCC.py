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

def encrpyt(text):
    print("encrypt")

def decrpyt(text):
    print("decrpyt")

# 1st. Take user input and handle the file
def handleFile(filename):
    text = ""
    with open(filename, 'r') as file:
        text = file.read()

    if "-scc" in text:
        decrpyt(text)
    else:
        encrpyt(text)


if __name__ == '__main__':
    print("="*24)
    filename = input("Please enter a filename: ")
    print("="*24)
    print("Processing...")
    #time.sleep(3) just cause it look cooler and legit
    handleFile(filename)
