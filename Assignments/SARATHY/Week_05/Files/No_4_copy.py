# 4. Write a program to read a file and copy it into a new
# Here we take the output file that we got from the previous problem



with open('file.txt','r') as f1:
	with open('file_copy.txt','w') as f2:
		f2.write(f1.read())
		
		
		
	