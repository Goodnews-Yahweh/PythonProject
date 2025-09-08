#!/bin/python
import random

food_list = ['jollof rice and turkey', 'beans and bread or garri', 'pizza', 'meat and chicken sauce', 'assorted meat']
print()

print("enter T to try again")
i = 1
while i <= 5:
    foodrn = random.choice(food_list)
    response = input(f"Would you like {foodrn}? (Y/N/T): ").upper()
    if response == 'Y':
        print(f"Have {foodrn}")
        break
    elif response == 'T':
        print()
        i += 1
        if i == 6:
            print("No food for you")
    else:
        print("No food for you")
        break
