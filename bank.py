
# Python Banking Program

# project to work with functions

def show_balance(balance):
    print('***********************')
    print(f"Your balance is: ${balance:.2f}¢")
    print('***********************')

def make_deposit():
    try:
        amount = float(input("Enter deposit: "))
        if amount < 0:
            print("You cannot deposit an amount that is less than zero!")
            return 0

        else:
            return amount
    except ValueError:
        print("Invalid, enter only numbers")

def withdraw(balance):
    try:
        amount = float(input("Enter the amount to withdraw: "))

        if amount > balance:
            print("Insufficient balance")
            return 0
        elif amount < 0:
            print("Amount must be greater than 0")
            return 0
        else:
            return amount
    except ValueError:
        print(f"Invalid '{amount}'")

def main():
    balance = 0
    is_running = True
    while is_running:
        print('*********************')

        print("*  Banking Program  *")

        print('*********************')

        print("1) Show Balance.")
        print("2) Make Deposit.")
        print("3) Withdraw.")
        print("4) Exit.")

        print('*********************')
        choice = input("Choose from the options above(1-4):" )
        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += make_deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print('*********************')
            print("Invalid, choose from the options above.")
            print('*********************')

    print('**************************')
    print("Thank you! Have a noice day")
    print('**************************')


if __name__ == "__main__":
    main()
