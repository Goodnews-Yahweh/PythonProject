
# Strings => ordered, immutable collection datatype, for txt representation.
# one most used datatype in Python

string:str = "Hello, World"
my_string = 'Hi, World'
my_str = """Hey
Whatsup doc? """

my_strin = """Hey, again \
howdy? """

print(string)
print(my_string)
print(my_str)
print(my_strin)
print()

#accessing the characters in a string
# by index
char:str = my_string[-1]
print(char)

# string slicing
x:int = input("x: ")
y:int = input("y: ")
z:int = input("z: ")

if x.isspace() and y.isspace() and z.isspace():
    print("them.isspace")

elif not (x.isalpha()) and not (y.isalpha()) and not (z.isalpha()):
    x = int(x)
    y = int(y)
    z = int(z)

    char:str= string[x:y:z]
    print("%s" %char)
else:
    print("Try again")


# concatenate strings
greet:str = "Howdy! "
name:str = "Tom"
greet_name:str = greet + name
print("%s" %greet_name)

# multiply str with a num
str = 'a'
num = 3
print(str * num)
print()

# iterate over a string with a for..in loop
for i in my_string:
    print(i)
print()

# check if a char is in a string
if 'q' in my_string:
    print("yes")
else:
    print("no")
