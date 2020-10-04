# 8. Write a script called diff.py that take two file names as arguments and checks if the content of
 #both the files is same and prints true or false.
 
import sys
with open(sys.argv[1],'r') as f1:
	file1=f1.read()
with open(sys.argv[2],'r') as f2:
	file2=f2.read()
if file1==file2:
	print("True")
else :
	print("False")


	