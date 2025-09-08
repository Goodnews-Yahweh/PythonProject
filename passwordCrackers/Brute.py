
import random
import time
import string
from getpass import getpass

# Input password
usr = getpass("Enter your password: ")

# All possible characters to guess from
characters = string.ascii_letters + string.digits + string.punctuation

# Simulate delay
print("Starting brute-force attack...")
time.sleep(2)

crack = ""
attempts = 0

while crack != usr:
    crack = ""
    for _ in range(len(usr)):
        crack += random.choice(characters)
    attempts += 1
    print(f"[Attempt {attempts}] {crack}")

print(f"\nPassword cracked: {crack} in {attempts} attempts!")
