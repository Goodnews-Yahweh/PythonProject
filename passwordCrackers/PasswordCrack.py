#!/bin/python

import random
#from random import *
import time

u_pwd = input("Enter password(4 combo): ")

pwd = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0 ]

pw=""

while(pw!=u_pwd):
    pw=""
    for letter in range(len(u_pwd)):
        guess_pwd = pwd[random.randint(0,19)]
        # pwd[randint(0,17)]
        pw = str(guess_pwd) + str(pw)
        print(pw)
        print("Cracking Password...Please wait")
       # time.sleep(0000000000000000000000.1)
    if pw == u_pwd:
        break

print("Your password is:", pw)

