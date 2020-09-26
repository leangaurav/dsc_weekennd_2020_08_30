
try:
    x = int(input("Enter a number:"))
    print("x=", x)
    b = 4//x
    print("b  = ", b)
    
except (ValueError,ZeroDivisionError) as err:
    print("Value Error or ZeroDivisionError")

print("End")