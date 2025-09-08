#!/bin/python

# random module
import random as ran
import time

# empty list
choices = {}
choices = set(choices)
# player entry
print("Let player name be only 7 characters.")
while True:
    player = input("Enter your player name: ").capitalize()
    if len(player) <= 7:
        print(f"Welcome, {player}")
        break
    else:
        print("Enter a Player Name of 7 characers")

print()
time.sleep(3)

# level 1
def level_1():
    #while loop
    while True:
        try:
            usr_input = int(input("Enter a number? "))
            choices.add(usr_input)
            if len(choices) == 2:
               #print(set(choices))
                break
            else:
                continue
        except ValueError:
            print("Enter numbers")
        except Exception:
            print("Something went wrong :(")
    time.sleep(2)

    while True:
        computer = ran.choice(list(choices))
        try:
            player = int(input(f"Choose a number from the list {choices}: "))
            if player == computer:
                print("You won.")
                print()
                print("R for repeat, M for move.")
                repeat = input("Do you want to play again or move to the next level(R/M)? ").upper()
                if repeat == 'R':
                    continue
                elif repeat == 'M':
                    print(f"You chose: {player}, and the computer chose: {computer}")
                    break
                else:
                    print("Enter either R/M")
            elif player not in choices:
                print("pick from the set list.")
            elif player != computer:
                print("You lose")
                rep = input("Do you want to try again(y/n)?").lower()
                if rep == 'y':
                    continue
                elif rep == 'n':
                    print(f"You chose: {player}, and the computer chose: {computer}")
                    break
                else:
                    print("Enter either y/n")
            else:
                print("Enter a valid number")
        except ValueError:
            print("pick a number")
#level_1()


def level_2():
    level_1()
    choices.clear()
    print()
    time.sleep(2)
    #while loop
    while True:
        try:
            usr_input = int(input("Enter a number? "))
            choices.add(usr_input)
            if len(choices) == 2**2:
                #print(set(choices))
                break
            else:
                continue
        except ValueError:
            print("Enter numbers")
        except Exception:
            print("Something went wrong :(")
    time.sleep(2)

    while True:
        computer = ran.choice(list(choices))
        try:
            player = int(input(f"Choose a number from the list {choices}: "))
            if player == computer:
                print("You won.")
                print()
                print("R for repeat, M for move.")
                repeat = input("Do you want to play again or move to the next level(R/M)? ").upper()
                if repeat == 'R':
                    continue
                elif repeat == 'M':
                    print(f"You chose: {player}, and the computer chose: {computer}")
                    break
                else:
                    print("Enter either R/M")
            elif player not in choices:
                print("pick from the set list.")
            elif player != computer:
                print("You lose")
                rep = input("Do you want to try again(y/n)?").lower()
                if rep == 'y':
                    continue
                elif rep == 'n':
                    print(f"You chose: {player}, and the computer chose: {computer}")
                    break
                else:
                    print("Enter either y/n")
            else:
                print("Enter a valid number")
        except ValueError:
            print("pick a number")


def level_3():
    level_2()
    choices.clear()
    print()
    time.sleep(3)
    #while loop
    while True:
        try:
            usr_input = int(input("Enter a number? "))
            choices.add(usr_input)
            if len(choices) == 2**3:
                #print(set(choices))
                break
            else:
                continue
        except ValueError:
            print("Enter numbers")
        except Exception:
            print("Something went wrong :(")
    time.sleep(2)

    while True:
        computer = ran.choice(list(choices))
        try:
            player = int(input(f"Choose a number from the list {choices}: "))
            if player == computer:
                print("You won.")
                print()
                print("R for repeat, M for move.")
                repeat = input("Do you want to play again or move to the next level(R/M)? ").upper()
                if repeat == 'R':
                    continue
                elif repeat == 'M':
                    print(f"You chose: {player}, and the computer chose: {computer}")
                    break
                else:
                    print("Enter either R/M")
            elif player not in choices:
                print("pick from the set list.")
            elif player != computer:
                print("You lose")
                rep = input("Do you want to try again(y/n)?").lower()
                if rep == 'y':
                    continue
                elif rep == 'n':
                    print(f"You chose: {player}, and the computer chose: {computer}")
                    break
                else:
                    print("Enter either y/n")
            else:
                print("Enter a valid number")
        except ValueError:
            print("pick a number")

level_3()

