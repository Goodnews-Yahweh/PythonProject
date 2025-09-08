# Unpacking in Python
# unpacking = refers to splitting up an iterable object and grabbing its individual elements.

# Basic unpacking
# list
my_list:list[int] = [1,2,3]
a,b,c = my_list
print("a: {}, b: {}, c: {}\n".format(a, b, c))

# tuple
my_tuple = (4,5,6)

i,j,k = my_tuple
print(f"i: {i}, j: {j}, k: {k}\n")

# set
my_set = {7,8,9}
x, y, z = my_set
print(f"x: {x}, y: {y}, z: {z}\n")

# string
my_string = "Hello"

p,q,r,s,t = my_string
print(f"p: {p}, q: {q}, r: {r}, s: {s}, t: {t}\n")

# dict
'''
my_dict = {'x':2, 'y':3}
a,b = my_dict
print(f"a: {a}, b: {b}\n")
'''

# Extended Iterable Unpacking with *

# * operator - allows us to collect multiple elements as a list/split up a list.
a_tuple = (1,2,3,4,5)

a,b,*c = a_tuple
print(f"a: {a}, b: {b}, c: {c}\n")

a,*b,c = a_tuple
print(f"a: {a}, b: {b}, c: {c}\n")

*a,b,c = a_tuple
print(f"a: {a}, b: {b}, c: {c}\n")


my_str:str = "Hello"

x, y, *z = my_str
print(f"x: {x}, y: {y}, z: {z}\n")

z1, z2, z3 = z
print(f"z1: {z1}, z2: {z2}, z3: {z3}\n")

movie = "Passion-of-Christ.mp4"

smovie = movie.split('.')

movie_name, movie_ext = smovie
print(f"{movie_name}\n{movie_ext}")

movie_p, movie_o,movie_c = movie_name.split('-')
print(movie_p)


# Ignoring Values
# using the anonymous variable(_)
# used when you need to put a variable somewhere but you don't actually want to access it later on

is_list = [1,2,3]

a,_,c = is_list
print(f"a: {a}, c: {c}")

_,_,c = is_list
print(f"c: {c}")

# Unpacking Nested Structures

