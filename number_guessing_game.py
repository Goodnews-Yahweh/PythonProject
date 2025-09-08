
# Python Number Guessing Game

from random import randint

# this is a range from lowest to highest number
lowest_num = 1
highest_num = 100
answer = randint(lowest_num, highest_num)

# To keep track of the number of guesses
guesses = 0

# Welcome Message
print("Welcome, to My Python Number Guessing Game")

print(f"Select a number from {lowest_num} to {highest_num}\n")

# To keep game running until the user quits or runs out of guesses

while guesses < 10:
    #Decided not to use try and except block for exception handling

    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        if guess < lowest_num or guess > highest_num:
            print("Number out of range!")
        elif guess > answer:
            print("Too High! Try again.")
            guesses += 1
        elif guess < answer:
            print("Too Low! Try again.")
            guesses += 1
        else:
            print("Congratulations, You guessed the right answer")
            print(f"{guesses} guesses\n")
            break
    else:
        print("Invalid, enter a valid guess=> number")
        guesses += 1
    print(f"Number of guesses: {guesses}\n")

