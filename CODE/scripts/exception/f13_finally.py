
try:
    x = int(input("Enter a number:"))
    print("x=", x)
    a = [10,20,0]
    a[x]
except ValueError as err:
    print("Please enter  only integers", err)
finally:
    print("This  will always run")

