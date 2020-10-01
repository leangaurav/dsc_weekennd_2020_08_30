import string
print('Start')
with open("temp.txt","r") as f1:
        content=f1.read()
        content1=content.split()
print(len(content1))
print('End')