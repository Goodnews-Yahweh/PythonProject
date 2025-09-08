
# Working with file objects in Python
# recommended
with open("python.txt","r") as f:

    size = 20
    p = 0

    file = f.read(size)

    print(file, end="")

    f.seek(p)

    file = f.read(size)
    print(file)


    #968 chars
