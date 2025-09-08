#!/bin/python

import random
from getpass import getpass
import string
import time

# Input password
usr_pwd = getpass("Enter password: ")
print(usr_pwd)

# All pissible characters to guess from
passwd = string.punctuation + string.digits + string.ascii_letters

# Simulate delay
print("Starting brute-force attack...")
time.sleep(2)

crack=""
attempts=0

while(crack != usr_pwd and not (usr_pwd.isspace())):
    crack=""
    for _ in range(len(usr_pwd)):
        crack += random.choice(passwd)

    print("Cracking Password...Please wait")
    attempts += 1
    print(f"[Attempt {attempts}] {crack}")
       
print(f"\nPassword cracked: {crack} in {attempts} attempts!")
