print("Start")

with open("file.txt", "r") as f:
    for line in f:
        print(line, end='')

print("\nEnd")