
# Collects user input

first_int = int(input("Enter your first integer: "))

second_int = int(input("Enter your second integer: "))

third_int = int(input("Enter your third integer: "))

sum = first_int + second_int + third_int

if first_int == second_int == third_int:
    sum *= 3
    print(sum)
else:
    print(sum)
