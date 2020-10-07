# 7. Modify the above program to count the occurrence of each symbol i.e. count of alphabet ‘a’,
#count of spaces, count of commas and so forth


import sys
occurence ={}
with open(sys.argv[1] ,'r') as f:
	for c in f.read():
		print(c)
		if c in occurence:
			occurence[c]+=1
		else :
			occurence[c]=1
	print(occurence)