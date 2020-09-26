print("Start")

f = open("file.txt", "r")

while True:
    content = f.read(4) # read 4  characters  from file
    
    if len(content) == 0:
        break
    print(content, end='')

f.close()
print("\nEnd")

