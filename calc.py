#!/bin/python

# addition
def addition():
    try:
        firstNumber = float(input("Enter a number: "))
        secondNumber = float(input("Enter another number: "))
        result = firstNumber + secondNumber
        print(f"{firstNumber} + {secondNumber} is: {result}")
    except ValueError:
        print("Invaid value/s\nEnter only numbers")
#addition()

# subtraction
def subtraction():
    try:
        firstNumber = float(input("Enter a number: "))
        secondNumber = float(input("Enter another number: "))
        result = firstNumber - secondNumber
        print(f"{firstNumber} + {secondNumber} is: {result}")
    except ValueError:
        print("Invaid value/s\nEnter only numbers")  

#subtraction()


# multiplication
def multiplication():
    try:
        firstNumber = float(input("Enter a number: "))
        secondNumber = float(input("Enter another number: "))
        result = firstNumber * secondNumber
        print(f"{firstNumber} * {secondNumber} is: {result}")
    except ValueError:
        print("Invaid value/s\nEnter only numbers")                                     

multiplication()

# division


# modulos


# floor division


# exponential
