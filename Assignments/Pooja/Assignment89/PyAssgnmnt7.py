import sys
print("Start")
with open(sys.argv[1],"r") as f:
   content=f.read()   
   for i in content:
     print(f'count of {i} is {content.count(i)}')
print(count1)
print("End")