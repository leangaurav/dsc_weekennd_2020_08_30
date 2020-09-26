print("Start")

f = open("file.txt", "r")

while True:
    content = f.readline()
    
    if len(content) == 0:
        break
    print(content, end='')

f.close()
print("\nEnd")