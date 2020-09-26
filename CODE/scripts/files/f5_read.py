print("Start")

f = open("file.txt", "r")

content = f.read() # returns all contents of file in form of a string
f.close()

print(content)

print()
print(repr(content))

print("\nEnd")

