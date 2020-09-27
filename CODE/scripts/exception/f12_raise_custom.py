
def func(x: int) -> int:
    if  x <= 0:
        raise ValueError("Func accepts only positive numbers > 0")
    res: float = 1/x
    return res
    
    
res = func(1)
res = func(1.5)
print(f"Res = {res}")