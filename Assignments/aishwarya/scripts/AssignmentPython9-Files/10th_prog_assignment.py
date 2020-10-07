f1 = open("file3.txt", "r")
data = f1.read().split()
print(data)
count = 0
for i in data:
    if i[::] == i[::-1]:
        count +=1
print("count of palindrome word",count) 