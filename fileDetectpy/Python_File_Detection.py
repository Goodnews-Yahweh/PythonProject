# Python File Detection
import os # this module provides a way for python programs to interact with the operating system

#file_path = "file.txt"

file_path = "/data/data/com.termux/files/home/downloads/text.txt"

if os.path.exists(file_path):
    print("The location '%s' exits" %file_path)
    if os.path.isfile(file_path):
        print("This is a file")
    elif os.path.isdir(file_path):
        print("This isn't a file")
        print("It is a directory")
        
    
else:
    print("That location doesn't exist")


