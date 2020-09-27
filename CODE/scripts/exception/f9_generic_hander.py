
def func1():
    try:
        x = int(input("Enter a number:"))
        print("x=", x)
        a = [10,20,0]
        b = a[x]
        return 4/b
    except ValueError:
        print("valueError")
    except Exception:
        print("Some error")
    return 0

def func2():
    try:
        x = func1()
        print("x  = ", x)
    except ZeroDivisionError as err:
        print("Exception in func2", err)

func2()
print("End")