import sys
with open(sys.argv[1],"r") as f1:
    content1=f1.read()
with open (sys.argv[2],"r") as f2:
    content2=f2.read()
print(content1==content2)
