
def kilo_to_poun(weight):
    weight = weight * 2.205
    unit = 'Lbs.'
    return f"Your weight is: %.2f {unit}" %weight


def poun_to_kilo(weight):
    weight = weight / 2.205
    unit = 'Kgs.'
    return f"Your weight is: %.2f {unit}" %weight

"""
def main():
    try:
        weight = float(input("Enter your weight: "))
        unit = input("Kilogram or Pounds(K/L)? ").upper()
        if unit == 'K':
            weight = kilo_to_poun(weight)
            print(weight)
        elif unit == 'L':
            weight = poun_to_kilo(weight)
            print(weight)
        else:
            pass
    except:
        pass


if __name__ == "__main__":
    main()
"""
