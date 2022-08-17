from decimal import DivisionByZero


a = 0
b = 10

while a < 4:
    print("----------------")
    a += 1
    b -= 1

    try:
        a / b
    except DivisionByZero:
        print(f"{a}, {b} - divided by zero")
        continue
    finally:
        print(f"{a}, {b} - always executes")
    
    print(f"{a}, {b} - main loop")
else:
    print("Code executed without a ZeroDivisionError")