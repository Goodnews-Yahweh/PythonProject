#!/bin/python3


food_store={
        'pizza': 20.9,
        'fried turkey': 10.0,
        'roasted chicken': 16.5,
        'ice cream': 15.5,
}

print(f"Available food stuffs:\n{food_store}")

item = input("What do you like to buy? ")
quantity = input("How many do you want to buy? ")
if item in food_store and quantity.isdigit():
    quantity = int(quantity)
    total = food_store[item] * quantity
    total = float(total)
    print(f"Your total is: ${total}¢")
else:
    print("Sorry we don't have this available in our store.")
    print("Have a noice day")
