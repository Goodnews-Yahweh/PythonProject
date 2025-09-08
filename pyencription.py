# Python Encryption Program

import random
import string

chars = " " +  string.punctuation + string.digits + string.ascii_letters


chars = list(chars)
key = chars.copy()

random.shuffle(key)

#print(f"chars: {key}")
#print(f"key: {key}")

#ENCRYPT
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for _ in plain_text:
    index = chars.index(_)
    cipher_text += key[index]

#print("Original message: %s" %plain_text)
print("Encrypted message: %s" %cipher_text)

#DECRYPT
cipher_text = input("Enter encrypted message: ")

plain_text = ""

for _ in cipher_text:
    index = key.index(_)
    plain_text += chars[index]

#print("Encrypted message: %s" %cipher_text)
print("Original message: %s" %plain_text)


