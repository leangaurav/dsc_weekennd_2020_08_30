import  sys
f = open(sys.argv[1], "r")
data2 = f.read()
count= 0
for i in data2:
    if i.isspace():
        count +=1
print(count)
