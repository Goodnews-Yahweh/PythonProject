
# Reading files in Python

try:
    with open("plans.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File does not exists :(")
