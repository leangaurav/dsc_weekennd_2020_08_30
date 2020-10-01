import sys
print("Start")
with open(sys.argv[1],"r") as f:
   content=f.read()
   count1=content.count(' ')
print(count1)
print("End")