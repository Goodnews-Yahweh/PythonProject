

def add(x, y):
    return x + y


def subtract(x,y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def calculate():
    print("Choose from the options")
    print("""1) +
2) -
3) *
4) /
""")

    operator = input("enter operator: ")
    for _ in operator:
        match operator:
            case '+':
                fnum = int(input("Enter fnum: "))
                snum = int(input("Enter snum: "))
                res = add(fnum, snum)
                print(res)
            case '-':
                fnum = int(input("Enter fnum: "))
                snum = int(input("Enter snum: "))
                res = subtract(fnum, snum)
                print(res)
            case '*':
                fnum = int(input("Enter fnum: "))
                snum = int(input("Enter snum: "))
                res = multiply(fnum, snum)
                print(res)
            case '/':
                fnum = int(input("Enter fnum: "))
                snum = int(input("Enter snum: "))
                res = add(fnum, snum)
                print(res)




if __name__ == "__main__":
    calculate()
