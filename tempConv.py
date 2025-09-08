#!/bin/python3

try:
    temp = float(input("Enter temperature: "))
    unit = input("Celsius or Fahrenheit(C/F)? ").upper()

    if unit == 'C':
        print()
        F = (9 * temp) / 5 + 32
        print("Fahrenheit: %.1f°F" %F)
    elif unit == 'F':
        print()
        C = (temp - 32) * 5 / 9
        print("Celsius: %.1f°C" %C)
    else:
        print()
        print("Invalid unit of temperature measurement.")
except ValueError:
    print()
    print("Invalid temp unit => number.")
