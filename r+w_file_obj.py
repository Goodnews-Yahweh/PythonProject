
# Reading and writing to a file in Python.


with open("file2.txt", "r") as rf:
    with open("file3.txt", "w") as wf:
        for line in rf:
            wf.write(line)
