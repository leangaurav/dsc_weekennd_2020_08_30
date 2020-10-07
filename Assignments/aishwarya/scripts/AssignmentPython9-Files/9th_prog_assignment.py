f1 = open("file1.txt", "r")
data = f1.read().split()
print(data)
print("count of word",len(data)) 