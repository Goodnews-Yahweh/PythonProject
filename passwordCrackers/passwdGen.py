
import random
import string

try:
    length = int(input("Enter password length: "))
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    number = string.digits
    symbols = string.punctuation

    all = lower + upper + number + symbols

    temp = random.choices(all, k=length)
    passwd = "".join(temp)
    print(passwd)

except ValueError:
    print("Enter numbers only")
