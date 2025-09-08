
# Weight Converter Program

try:
    weight = float(input("Enter your weight: "))
    unit = input("Kilogram or Pounds(K/L)? ").upper()
    if unit == 'K':
        print()
        weight = weight * 2.205
        unit = 'Lbs.'
        print(f"Your weight is: %.2f {unit}" %weight)
    elif unit == 'L':
        print()
        weight = weight / 2.205
        unit = 'Kgs.'
        print(f"Your weight is: %.2f {unit}" %weight)
    else:
        print()
        print("Invalid unit of weight measurement '%s'" %unit)
except ValueError:
    print()
    print("Invalid weight value")
    print("Enter valid weight value => number")
except Exception:
    print()
    print("Something went wrong :(")

