
# INTERMEDIATE PYTHON
# Tuples in PYTHON
# Tuple = collection datatype, ordered, immutable, and allows for different datatype and duplicate elements

mytuple:tuple= ('Goody',18,'UK')

my_tuple:tuple= tuple(['Goody',18,'UK'])

mytup = 'Max', 21, 'Boston'

mytup2 = ('Max') # str

mytup3 = ('Bro', ) # tuple


print(mytuple)

# find length of tuple
mytuple_length: int = len(mytuple)
print(f"{mytuple_length = }")
print()

# access a tuple's element
mytuple_in = mytuple[1]
mytuple1: str = mytuple.index(18)
print(mytuple_in)
print()

# count number of occurrence of an element in a tuple

mytuple1:tuple[str]= ('b','l','u','e','b','e','r','r','y')

print(mytuple1.count('r'))
print()

# loop through a tuple
for x in mytuple:
    print(x)
    print()

# slice a tuple
mytuple2 = mytuple1[4:]
print(mytuple2)
print()

# check element in tuple

if "Goody" in mytuple:
    print("yes")
else:
    print("no")

print()

# change a tuple to a list and vice versa
mylist = list(mytuple)
mytuple = tuple(mylist)
print(mylist)
print(mytuple)
print()


# unpack a tuple
print(mytuple)
name, age, city = mytuple
print(name)
print(age)
print(city)
print()

# difference between a tuple and a list

import sys
import timeit

# size of tuple and list
my_tuple = ("Max",18,"Nigeria", True)
my_list = ["Max",18,"Nigeria",True]

print(sys.getsizeof(my_tuple), "bytes")
print(sys.getsizeof(my_list), "bytes")
print()

# speed of tuple and list
print(timeit.timeit(stmt="(0,1,2,True)",number= 1000000), "secs")
print(timeit.timeit(stmt="[0,1,2,True]",number= 1000000), "secs")


