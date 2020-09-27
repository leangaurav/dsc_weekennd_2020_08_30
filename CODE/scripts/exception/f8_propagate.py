
def func1():
    try:
        x = int(input("Enter a number:"))
        print("x=", x)
        a = [10,20,0]
        return a[x]
    except ValueError:
        print("Please enter  only integers")
    return 0

def func2():
    try:
        x = func1()
        b = 4//x
        print("b  = ", b)
    except ZeroDivisionError as err:
        print("Exception in func2", err)

func2()
print("End")