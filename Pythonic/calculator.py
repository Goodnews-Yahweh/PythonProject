# Basic Calculator
import calc

def calculator() -> None:
    opdict:dict = {
        1:'+',
        2:'-',
        3:'*',
        4:'/',
        5:'%',
        6:'//',
        7:'**',
    }
    for x,y in opdict.items():
        print(f"{x} : {y}")
    try:
        fnum: float = float(input("Enter first number: "))
        operator: str = input("choose an operator(from above): ")
        snum:float = float(input("Enter second number: "))
        if operator == opdict[1]:
            add = calc.add(fnum, snum)
            print(add)
        elif operator == opdict[2]:
            sub = calc.sub(fnum, snum)
            print(sub)
        elif operator == opdict[3]:
            mul = calc.mul(fnum, snum)
            print(mul)
        elif operator == opdict[4]:
            div = calc.div(fnum, snum)
            print(div)
        elif operator == opdict[5]:
            mod = calc.mod(fnum,snum)
            print(mod)
        elif operator == opdict[6]:
            fdiv = calc.fdiv(fnum, snum)
            print(fdiv)
        elif operator == opdict[7]:
            exp = calc.exp(fnum, snum)
            print(exp)
    except ValueError:
        print("Enter a number please.")

if __name__ == "__main__":
    calculator()
