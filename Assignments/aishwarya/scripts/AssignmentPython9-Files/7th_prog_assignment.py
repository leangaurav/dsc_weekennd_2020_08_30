import  sys
f = open(sys.argv[1], "r")
data2 = f.read()
d = {}
for i in data2:
    if i  in d.keys():
        d[i] = d[i]+1
    else :
        d[i] = 0
print(d)

    
