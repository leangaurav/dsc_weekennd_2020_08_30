def func1():
    try:
        x = int(input("Enter a number "))
        a = [10,20,0]
        b = a[x]
        return 4/b
    except ValueError:
        print("Value Error")
    except Exception:
        print("Some Error")
        return 0
def func2():
    try:
        x = func1()
        print("x =",x)
    except ZeroDivisionError as err:
        print ("zerodivisionerror",err)
func2()