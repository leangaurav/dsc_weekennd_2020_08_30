# 5. Write a program to read a file and copy the contents 
# to a new file such that the case gets
# reversed. i.e. upper case becomes lower case and vice versa.

with open('readfile.txt', 'r') as f_read:
	with open('writefile.txt' , 'w') as f_write:
		to_write=''
		for i in f_read.read():  
			if i.isalpha() == False: # for \n and digits
				to_write = to_write + i
			if i.islower():
				to_write = to_write + i.upper()
			if i.isupper():
				to_write = to_write + i.lower()
		f_write.write(to_write)