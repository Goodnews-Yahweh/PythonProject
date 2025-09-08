#!/bin/python3

global food_store

food_store = {
        'pizza': 45.5,
        'fried turkey': 50.5,
        'roasted chicken': 45.3,
        'ice cream': 23.5,
        'ice cream sundae': 234.56,
}

#print(f"Available food in store:\n{food_store}")


def current_account():
    global current
    current = 0
    try:
       putin = float(input("How much do you want to put in your current account (in dollars)? "))              
       if putin >= 1 and putin <= 10_000:
           current = putin
           print(f"Cash at bank is: ${current}¢")
       elif putin < 1:                                   print("You cannot put in money less than $1")
       elif putin > 10_000:
           print("Money in current account should not be more than ten thousand")
       else:
           print("Invalid\nEnter a number")
    except ValueError:                               print("Invalid\nEnter a valid number")
    except Exception:                                  print('Something went wrong :( ')

def savings_account():
    current_account()
    global savings
    savings = 0
    try:
        savings = float(input("How much do you want to use from your current_account? "))
        if savings < current and savings != 0:
           savings = savings
           print(f"Savings account is: ${savings}¢")
        elif savings > current:
            print("You cannot save more than what you have with")
        elif savings == 0:
            print("What are you saving?")
    except ValueError:
        print("Invalid\nEnter a valid number")
    except Exception:
        print("Something went wrong :( ")

savings_account()

print()
print(f"Available food stuffs:\n{food_store}")
item = input("What would you love to buy? ")
quantity = input("How many do you want to buy? ")
if item in food_store and quantity.isdigit():
    quantity = int(quantity)
    total = food_store[item] * quantity
    if total < savings or total == savings:
       print("You have purchased {quantity} x {item}/s")
       print(f"The total is: ${total: .2f}¢")
       pay = input("Do you want to continue order (Y/N)?").upper()
       if pay == 'Y':
          savings = savings - total
          print(f"You bought: {quantity} x {item}/s")
       else:
               print("Order cancelled")
    elif total > savings:
           print("Unable to purchase due to low amount in bank")
    else:
           print("Invalid")
else:                                           print("Sorry we don't have this available in our store.\nHave a noice day") 

