
# Useful String Methods in Python.

my_string = "  Hello, World!  "
# .strip() to remove whitespaces
my_string = my_string.strip()
print("%s" %my_string)

# change all chars in a string to uppercase
# .upper()
print(my_string.upper())

# change all chars in a string to lowercase
# .lower()
print(my_string.lower())

# .startswith()
str = "My name is Goodnews"

if str.startswith('M'):
    print(True)
else:
    print(False)

# .endswith()
if str.endswith('s'):
    print(True)
else:
    print(False)


# .find()
print(my_string.find('W'))

# .count()
print(my_string.count('l'))

# .replace()
my_string:str = my_string.replace("World", "Universe")

my_string:str = my_string.replace("Hello", "Hi")

print(my_string)

# change a string to a list
my_string:str = "how are you doing"
my_list:list[str] = my_string.split()
print(my_list)

my_str = "080-341-007-890"
my_list = my_str.split('-')
print(my_list)
