
# basic calculator module in Python

def add(a:float, b:float) -> float:
    return a + b

def sub(a: float, b:float) -> float:
    return a - b

def mul(a: float, b: float) -> float:
    return a * b

def div(a:float, b:float) -> float:
    if b == 0:
        return "Error divison by zero"
    else:
        return a / b

def mod(a: float, b:float)-> float:
    if b == 0:
        return "Error divison by zero"
    else:
        return a % b
def fdiv(a:float, b:float) -> float:
    if b == 0:
        return "Error divison by zero"
    else:
        return a // b

def exp(a: float, b: float) -> float:
    return a ** b

