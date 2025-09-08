
# Greetimg program in Python

from datetime import datetime


def morning(name: str) -> str|None:
    return f"Good morning, {name}"


def afternoon(name: str) -> str|None:
    return f"Good afternoon, {name}"

def evening(name:str) -> str|None:
    return f"Good evening, {name}"

def greet() -> None:
    name: str = input("What is your name? ")

    a: int = 00
    b: int = 00
    c: int = 00

    

    i: int = 12
    j: int = 00
    k: int = 00

    while i<=16 and j<=59 and k<=59:
        afternoon: str = str(f"{i}:{j}:{k}")
        i += 1
        j += 1
        k += 1
    
    x: int = 17
    y: int = 00
    z: int = 00

    while x<=23 and y<=59 and z<=59:
        evening:str = str(f"{x}:{y}:{z}")
        x += 1
        y += 1
        z += 1


    current_time = datetime.now().strftime("%H:%M:%S")
    if morning >= current_time:
        print(morning(name))
    elif afternoon >= current_time:
        print(afternoon(name))
    elif evening >= current_time:
        print(evening(name))
    else:
        print("Timer out of zone")

if __name__ == "__main__":
    greet()



