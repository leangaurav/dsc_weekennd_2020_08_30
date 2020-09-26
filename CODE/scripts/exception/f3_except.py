
try:
    x = int(input("Enter a number:"))
    print("x=", x)
    b = 4//x
    print("b  = ", b)
    
except Exception as err:
    print("Something went wrong!", err)

print("End")