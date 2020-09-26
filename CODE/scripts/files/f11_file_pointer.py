print("Start")

with open("file.txt", "r") as f:

    print("file Pointer:", f.tell())
    r = f.read()
    print("file Pointer:", f.tell())
    print(repr(r))
    
    print()
    f.seek(0)
    r = f.read()
    print(repr(r))

print("\nEnd")


# abcdefgh12345678
#                 ^