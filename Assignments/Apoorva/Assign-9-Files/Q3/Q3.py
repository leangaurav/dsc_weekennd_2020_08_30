#3. Predict output of the following piece of code:

"""
0 
line 
4	  
"""

f = open ('file','w')
f.write('line with some characters')
f.close()

f= open('file','r')
print(f.tell())
print(repr(f.read(4)))
print(f.tell())
