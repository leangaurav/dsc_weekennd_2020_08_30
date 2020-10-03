# 4. Write a program to read a file and copy it into a new file.

print('readfile.txt => writefile.txt ')
with open('readfile.txt','r') as f_read:
	with open('writefile.txt','w') as f_write:
		f_write.write(f_read.read())