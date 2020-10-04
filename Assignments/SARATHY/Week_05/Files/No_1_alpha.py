# 1. Write a program in python that stores alphabets from a to z in a text file

import string
with open('alpha.txt','w') as f:
    for i in string.ascii_lowercase:
        f.write(i+'\n')
   
		
   
		
    
