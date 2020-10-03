# 8. Write a script called diff.py that take two file names as arguments and 
# checks if the content of
# both the files is same and prints true or false.

import sys

with open (sys.argv[1],'r') as f1:
	with open (sys.argv[2],'r') as f2:
		if f1.read() == f2.read():
			print('True')
		else:
			print('False')