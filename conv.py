#!/bin/python3

print("Enter 0 to break out!")
while True:
    user_input = input("Enter something >>> ")
    if user_input == '0':
        break
    else:
        print(f"You entered: {user_input}")
print("Program exe at 0x0")
