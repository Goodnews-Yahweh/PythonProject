#!/bin/python3

import random
import time

pick = {}
pick = set(pick)

while True:
    try:
        l = int(input("How many numbers should the list contain? "))
        if bool(l) == True or bool(l) == False:
            print()
            time.sleep(2)
            break
    except ValueError:
        print("enter a number")
while True:
    try:
        add = int(input('Enter some numbers: '))
    except ValueError:
        print("emter some numbers")

    pick.add(add)
    if len(pick) == l:
        pick = tuple(pick)
        #print(pick)
        break
time.sleep(2)
print()

i = 1

if l > 4:
    while i <= 7:
        com = random.choice(pick)
        try:
            play = int(input("Guess the cotrect number? "))
        except ValueError:
            print("enter only number/s")
        if play == com:
            print('Congrats!, You won')
        elif play != com:
            rep = input("Do you want to try again? (Y/N)").upper()
            if rep != 'N':
                i += 1
            else:
                break
        else:
            print("Enter number within the range!")
            i += 1

elif l < 4:
    while i <= 3:
        com = random.choice(pick)
        try:
            play = int(input("Guess the cotrect number? "))
        except ValueError:
            print("enter only number/s")
        if play == com:
            print('Congrats!, You won')
        elif play != com:
            rep = input("Do you want to try again? (Y/N)").upper()
            if rep != 'N':
                i += 1
            else:
                print("Enter number within the range!")

else:
    print("Something went wrong")
