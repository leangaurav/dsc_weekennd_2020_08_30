
try:
    x = int(input("Enter a number:"))
    print("x=", x)
    b = 4//x
    print("b  = ", b)
    
except ValueError:
    print("Please enter  only integers")
except ZeroDivisionError:
    print("Don't enter a zero")

print("End")