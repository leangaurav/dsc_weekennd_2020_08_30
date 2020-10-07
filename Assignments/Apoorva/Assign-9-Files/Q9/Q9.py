# 9. WAP to count the number of words in a file.

c = 0
with open('readfile.txt','r') as f_read:
	for i in f_read.read():
		if i.isspace():
			c+=1
print("Number of words: ",c+1)