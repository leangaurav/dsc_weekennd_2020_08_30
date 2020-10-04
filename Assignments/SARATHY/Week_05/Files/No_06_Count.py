# 6. Write a program that take a file name as command line argument, opens it and then counts
# number of space characters in that file.

import sys
with open(sys.argv[1],'r') as f1:
	print(f1.read().count(" "))