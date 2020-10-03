
import sys
c = {}
with open(sys.argv[1],'r') as f_read:
	for i in f_read.read():
		if i in c.keys():
			c[i] +=1
		else:
			c[i] = 1
print(c)