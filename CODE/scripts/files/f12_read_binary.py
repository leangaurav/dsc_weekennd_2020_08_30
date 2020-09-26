with open('file.txt', 'r') as f:
    r = f.read()
    print(type(r), repr(r))
    
with open('file.txt', 'rb') as f:
    r = f.read()
    print(type(r), r)