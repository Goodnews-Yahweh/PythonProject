#Exceptions in Python

#x = 'hi'

try:
    x += 5
    print(x)
except Exception as e:
    print(e)
else:
    print('No error occurred, program completed')
finally:
    print("I don't care about the errors")


# we want to create water molecule
hydrogen_mole = 2
oxygen_mole = 7

if hydrogen_mole > oxygen_mole:
    print("Water molecule created")
else:
    raise Exception("H < O")

