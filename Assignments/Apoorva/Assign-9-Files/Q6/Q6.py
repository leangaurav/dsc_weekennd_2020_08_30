#6. Write a program that take a file name as command line
#  argument, opens it and then counts
# number of space characters in that file.


import sys
c = 0
with open(sys.argv[1],'r') as f_read:
	for i in f_read.read():
		if i.isspace():
			c+=1

	print("The number of spaces ",c)