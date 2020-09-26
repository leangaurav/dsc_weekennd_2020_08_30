
try:
    x = int(input("Enter a number:"))
    print("x=", x)
    b = 4//x
    print("b  = ", b)
    
except ValueError:
    print("Please enter  only integers")

print("End")