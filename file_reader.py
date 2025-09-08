

# File reader in Python

print("File must be in the same directory with the python script.\n")

file = input("Enter filename in: ")
try:
    with open(file, "r") as rf:
        for line in rf:
            print(line, end='')
except FileNotFoundError:
    print("""Oops file not found!
Either it not in this directory or it does not exist""")
