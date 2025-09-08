#!/bin/python

import random
from getpass import getpass
import string

usr = input("Want to generate random passwd(Y/N)? ").upper()
if usr == 'Y':
    global usr_pwd
    try:
        usr_pwd = ""
        length = int(input("Enter password length: "))
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        number = string.digits
        symbols = string.punctuation
        all = lower + upper + number + symbols
        temp = random.sample(all, length)
        passwd = "".join(temp)
        usr_pwd = passwd
    except ValueError:
        print("Enter numbers only")
else:
    if usr == 'N':
        usr_pwd = getpass("Enter password: ")

passwd = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k','l','m','n','o','p','q','','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',',','.','*','"','\'',':',';','!','?','(',')','/','+','-','&','_','$','#','@','|','~','`', '•','√','π','÷','×','§','∆','\\','{','}','=','°','^','¥','∞','€','¢','£','%','©','®','™','✓','[',']','<','>','Ω','—', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0 ]

crack=""

while(crack != usr_pwd and not (usr_pwd.isspace())):
    crack=""
    for i in range(len(usr_pwd)):
        guess_pwd = passwd[random.randint(0,113)]
        # pwd[randint(0,17)]
        pwd = str(guess_pwd)
        crack += pwd
        print(crack)
        print("Cracking Password...Please wait")


print(f"Your Password is: {crack}")
