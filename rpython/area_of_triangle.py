

# Python script to calculate area of a triangle with known sides

try:
    # collects user input for area of triangle computation
    a = float(input("Enter side a: "))
    b = float(input("Enter side b: "))
    c = float(input("Enter side c: "))

    #  Heron's formula
    #1 find semi perimeter

    s = (a + b + c) / 2

    #2 find the area

    # calculate the area
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

    print(round(area,2))
    #print(s)

except ValueError:
    print("Invalid\nEnter a number for the sides")

