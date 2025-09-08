
# inbuilt math functions

# round, abs, pow, max, min

result1 = round(3.141)
print("result1: %d" %result1)
print()

result2 = round(158.25239875849, 3)
print("result2: %f" %result2)
print()

result3 = abs(-100)
print("result3: %d" %result3)
print()

result4 = pow(2, 6)
print("result4: %d" %result4)
print(f"%d GB DDR5 RAM, and x{80 + 6}_x{result4}" %result4)
print()

x, y, z = 5, 7, 3.14

result5 = min(x, y, z)
print("result5: %.2f" %result5)
print()

result6 = max(x, y, z)
print("result6: %d" %result6)
print()

if max(x, y, z) == x:
   print(f"{x} is the max number")
elif max(y, x, z) == y:
   print(f"{y} is the max number")
elif max(y, x, z) == z:
   print(f"{z} is the max number")
else:
   print(f"None is the max number")
