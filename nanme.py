#!/bin/python

name = input("Enter your name>> ")

if name == "":
    print("You did not type in your name")
elif name.isspace():
    print("You did not type in your name")
else:
    print("Hello, %s" %name)

