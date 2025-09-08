
num = []

while True:
    x = int(input("Emter numbers: "))
    num.append(x)
    if len(num) == 2:
        print(num)
        break


for i in range(5):
    num[0] = i
    print(num[1])


