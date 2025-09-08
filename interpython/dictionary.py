
# INTERMEDIATE PYTHON
# Dictionaries in PYTHON

# Dictionary: collection datatype,unordered, mutable, consists of key-value pairs.

mydict:dict= {"name":"Goody","age":18,"city":"Zion"}

mydict2:dict= dict(name="Bro", age=21, city="US")

# Access the value in a dictionary.
value:str = mydict["name"]
print(value)

# Add a new key-value pair to a dictionary
mydict["email"] = "goody@xyz.com"
#print(mydict)

mydict["email"] = "coolgoody@xyz.com"
print(mydict)

'''
# delete from a dictionary
# (1) del keyword
del mydict["email"]
print(mydict)
# (2) .pop(key)
fromdict = mydict.pop("name")
print(fromdict)
print(mydict)

# (3) .popitem()
mydict.popitem()
print(mydict)
'''
print()
# check if a key is in a dictionary
# (1) if...in stmt

if "name" in mydict:
    print("name is in mydictionary")
    print(mydict["name"])
    print()
else:
    print("name is not in mydicitonary")
    print()

# (2) use a try...except block
try:
    print(mydict["lastname"])
    print()
except KeyError:
    print("Key Error!?")
    print()

# loop/iterate through a dictionary
# for...in loop

"""
# for each key in the dictionary
for key in mydict.keys():
    # 1. can use only mydict
    # 2. can use another word  aside key like x, etc.
    print(key)
    print()

# for each value in a dictionary
for value in mydict.values():
    # 1. cannot use only mydict
    # 2. can use another word aside value like y, etc.
    print(value)
    print()
"""
# for both key and value
for key,value in mydict.items():
    print(f"{key:5}:{value}")
    print()

# copy a dictionary
# 1. use .copy()
mydict_cpy:dict= mydict.copy()
#print(mydict_cpy)

# 2. use dict()
mydict_cpy2:dict = dict(mydict)
#print(mydict_cpy2)

# merge a dictionary
mydict.update(mydict2)
print(mydict2)
print(mydict)
print("\n")

################ more ################
x:tuple[int]= (2,3,4,5,0)
y:tuple[int]= (1,6,7,8,9)
l:list[int] = [23,54]
s:set[str] = {'a','e','i','o','u'}
l1:list[str] = ['a','s','d','f']
d:dict= {x:10, 'tuple':y, x:s, y:l1}
print(d)
