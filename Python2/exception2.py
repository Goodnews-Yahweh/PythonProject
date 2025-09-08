
x = 'hi'
x = 5

# how to find exception type
try:
    x += 5
    print(x)
    try:
        print(i)
    except Exception as x:
        print(f"Exception type: {type(x).__name__}")
        
except Exception as e:
    print(f"Exception type: {type(e).__name__}")
    x = None
    
finally:
    try:
        for k in range(1000000000000):
            print(k)
    except KeyboardInterrupt as e:
        print(e)
