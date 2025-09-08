
from datetime import datetime as dt
import random

a:list[int] = [0,1,2,3,4,5,6,7,8,9,10,11,12]

x: list[int] = [18,19,20,21,22,23]


i:list[int] = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59]

morn = f"{a}:{i}:{i}"
morn = random.choice(morn)
even = f"{x}:{i}:{i}"
even = random.choice(even)

current_time = dt.now().strftime("%H:%M:%S")

if current_time ==  morn:
    print("Good morning")
elif current_time ==  even:
    print("Good evening")
else:
    print("time not known")
#print(current_time)
