# 5. Write a program to read a file and copy the contents to a new file such that the case gets
#reversed. i.e. upper case becomes lower case and vice versa


with open('alpha.txt','r')	as f1:
	with open('alpha_case_reverse.txt','w') as f2:
		f2.write(f1.read().swapcase())