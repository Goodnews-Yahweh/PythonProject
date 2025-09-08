
#INTERMEDIATE PYTHON
# SETS IN PYTHON
# sets: collection datatype, unordered, mutable, no duplicates

# a set in Python is an unordered collection datatype of unique elements.

myset: set = set()

# add elements to a set
myset.add(1)
myset.add(2)
myset.add(3)
myset.add(4)

# remove elements from a set
# 1. .remove()
# can throw error
myset.remove(4)

# doesn't throw error
# 2. .discard()

myset.discard(3)

# 3. .pop()
#returns a value
print(myset.pop())


# clear a set
myset.clear()
#print(myset)


myset: set = (1,2,3,4,5)

print(myset)

# iterate over a set
# for...in loop
for s in myset:
    print(s)
print()

# check if an element is in a set
# if...in statement
if 1 in myset:
    print("yes")
else:
    print("no")
print()

evens:set = {0, 2, 4, 6, 8}
odds:set = {1, 3, 5, 7, 9}
primes:set = {2, 3, 5, 7, 11}

# union of sets
# 1. slower with .union()
union:set = odds.union(evens)
print(f"{union = }")

# 2. faster with |

union2:set = primes | odds
print(f"{union2 = }")
print()

# intersection of sets
# 1. slower with .intersection()
intersect:set = odds.intersection(primes)
print(f"{intersect = }")

# 2. faster with the &
intersect2:set = evens & primes
print(f"{intersect2 = }")
print()

# Difference of sets
setA:set = {1,2,3,4,5,6,7,8,9}
setB:set = {1,2,3,10,11,12}

# 1. .difference()
set_diff:set = setB.difference(setA)
print(set_diff)

# 2. .symmetric_difference

set_sys_diff:set[int] = setA.symmetric_difference(setB)
print(set_sys_diff)

print()
setAA = setA.copy()
setBB = setB.copy()

# to do update
#1. .update()

#setA.update(setB)
#print(setA)

#2. .intersection_update()
#setA.intersection_update(setB)

#print(setA)
#print(setB)

#3. .difference_update()
setAA.difference_update(setBB)
print(setAA)


#4. .symmetric_difference_update()
setA.symmetric_difference_update(setB)
print(setA)


# to check Superset and Subset
setX = {1,2,3,4,5,6}
setY = {1,2,3}
setZ = {7,8}

# .issubset()
if setX.issubset(setY):
    print(f"setX < setY = True")
else:
    print("setX !< setY = False")


# .issuperset()
if setX.issuperset(setY):
    print("setX > setY = True")
else:
    print("setX !> setY = False")

#isdisjoint()
# means null intersection i.e, no same element in both sets.

if setX.isdisjoint(setZ):
    print("setX !& setZ")
else:
    print("setX & setZ")


# Frozenset => immutable set, collection datatype
# frozenset()

a = frozenset([1,2,3,4,5])
print(a)
