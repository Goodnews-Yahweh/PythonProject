
# Consession Stand Program in Python

# dict = {key: value}

menu = {"pizza": 10.45,
        "pop corn": 5.00,
        "hot dog": 2.55,
        "pretzel": 3.00,
        "candy": 1.50,
        "soda": 3.50,
        "bottle water": 1.00,
        "shawarma": 20.09,}

cart = []
total = 0


print("--------MENU--------")
for key, value in menu.items():
    print(f"{key:10}: £{value:.2f}")

print("--------------------")

while True:
    food = input("Select an item(q to quit): ").lower()

    if food == 'q':
        break
    elif menu.get(food) is not None:
        cart.append(food)
print()
print("---------YOUR ORDER---------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
quantity = input("How many? ")
if quantity.isdigit():
    quantity = int(quantity)
    print(f"You bought: {quantity} x {food}/s")
    print(f"Total is: £{total:.2f}")
else:
    print("invalid")

