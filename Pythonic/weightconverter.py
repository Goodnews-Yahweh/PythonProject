
import weightconv

def main():
    try:
        weight = float(input("Enter your weight: "))
        unit = input("Kilogram or Pounds(K/L)? ").upper()
        if unit == 'K':
            weight = weightconv.kilo_to_poun(weight)
            print(weight)
        elif unit == 'L':
            weight = weightconv.poun_to_kilo(weight)
            print(weight)
        else:
            pass
    except:
        pass


if __name__ == "__main__":
    main()
