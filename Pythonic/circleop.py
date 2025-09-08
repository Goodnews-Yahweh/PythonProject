#!/bin/python

from math import pi

# given radius
try:
   radius = float(input("Enter the radius of the circle: "))
   r = radius
except ValueError:
	print("Enter only number(s)")

# choice
print("Enter A/C/D")
cal = input("Do you want to find the area or circumference or diameter of a circle? ").upper()


# 1st expression
if cal == "C":
   circumference = 2 * pi * r
   c = circumference
   print(f"cirvum: {c}cm")
   f = input("Do you want to round, enter to what decimal place? ")
   if f.isdigit():
      df = int(f)
      print(f'Circumference of the circle is: {round(c, df)}cm')
   else:
      print("enter only numbers")
# 2nd expression
elif cal == "A":
     area = pi * pow(r,2)
     print(f"area: {area}cm²")
     f = input("Do you want to round it, enter how many decimal places? ")
     if f.isdigit():
        df = int(f)
        print(f'Area of the circle is: {round(area, df)}cm²')
     else:
        print("enter only numbers")

# 3rd expression
elif cal == 'D':
    diameter = 2 * pi * pow(r,2)
    print(f"Diameter: {diameter}cm")
    f = input("Do you want to round it, enter how many decimal places? ")
    if f.isdigit():
        df = int(f)
        print(f'Diameter of the circle is: {round(diameter, df)}cm')
    else:
        print("enter only numbers")

