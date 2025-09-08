
import os

# Python script that allows users to write simple files

print("WARNING, this can overwrite existing files.\n")

file = input("Enter the name of file you want to write to: ")

try:
    with open(file, "x") as wf:
        write = input("Enter what you want to write:\n")
        wf.write(write)
except FileExistsError:
    print("****file exist****\n")
    with open(file, "r") as rf:
        file_read = rf.read(15)

        while len(file_read) > 0:
            print(file_read, end="")
            if len(file_read) == 0:
                print(file_read, end="\n")
            file_read = rf.read()

        write = input("\n\ndo you want to overwrite the file contents(Y/N)?")
        if write.upper() == "Y":
            overwrite= input("Enter what you want to write:\n")
            with open(file, "w") as wf:
                wf.write(overwrite)

                
