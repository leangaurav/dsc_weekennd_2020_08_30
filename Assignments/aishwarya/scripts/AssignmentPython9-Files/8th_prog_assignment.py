import sys
f1 = open (sys.argv[1], "r")
data1 = f1.read()
f2 = open (sys.argv[2], "r")
data2 = f2.read()
print(data1 == data2)