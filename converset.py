#!/bin/python3

import time

users = []

start = input("Do you want to start conversation? (Y/N):").upper()
time.sleep(2)
print()

if start == 'Y':
    while True:
        print('Enter 0 to stop.')
        useradd = input("Enter your name: ").capitalize()
        users.append(useradd)
        if len(users) == 2:
            #users.append(useradd)
            print(f"Users: {users}")
            break
        elif useradd == '0':
            print(f"Users: {users}")
            break
        #elif len(users) == 2:
           # print(f"Users: {users}")
            #break
        else:
            pass
else:
    if start == 'N':
        print("Okay")



