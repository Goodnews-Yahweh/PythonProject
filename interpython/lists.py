#!/bin/python3
# Intermediate Python
# Lists in Python

mylist:list[str] = ['banana','cherry','apple']

print(mylist)

# access an element
item:str = mylist[2]
#print(item)

for i in mylist:
    print(i)

# find the length of a list
print(f"mylist length: {len(mylist)}")

# check element in list
if 'banana' in mylist:
    print("yes")
    print()
else:
    print("no")
    print()
# append to a list
mylist.append('strawberry')
print(mylist)
print()

# insert to a list by index
mylist.insert(2, 'blueberry')
print(mylist)
print()

# remove from a list
mylist.remove('banana')
print(mylist)
print()

# pop a list
mylist2: str = mylist.pop()
print(mylist2)
print(mylist)

mylist.pop(2)
print(mylist)
print()

# renew mylist
mylist.append('strawberry')
mylist.append('banana')
mylist.append('apple')
mylist.append('mango')
print(mylist)
print()

# sort a list
mylist3 = sorted(mylist)
print(mylist3)
print(mylist)
print()

# copy a list
# (1) .copy()
list_cpy = mylist.copy()
# (2) list()
list_cpy2 = list(mylist)
# (3) indexing
list_cpy3 = mylist[:]

print(list_cpy)
print()

# clear a list
mylist.clear()
print(mylist)
print()

# del a list
del mylist
#print(mylist)

print()

# reverse a list
mylist3.reverse()
print(mylist3)
print()

############## PART 2 #################
num_list:list[int]= [1,2,3,4,5,6,7,8,9,0]

# create list with same elements
num: list[int] = [2] * 10
print(num)
print()

# check max number
max_num_in_num_list:int= max(num_list)
print(f"{max_num_in_num_list = }")
print()

# check min number
min_num_in_num_list:int= min(num_list)
print(f"{min_num_in_num_list = }")
print()

# sum a list
sum_of_num_list:int= sum(num_list)
print(f"{sum_of_num_list = }")
print()

# list comprehension
list_num:int= [x for x in num_list]
print(list_num)
print()

# square of all elements in num_list
list_num2:int= [x*x for x in num_list]
print(list_num2)
print()
