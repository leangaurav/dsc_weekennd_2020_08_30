def add(x,y):
    return x + y

def sub(x,y):
    return x - y

if __name__ == "__main__": # check if script is being imported or executed directly
    print("Module: ", __name__)
    print("Module", add(10,20))