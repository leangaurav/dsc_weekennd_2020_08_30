s= 'Python is object oriented'
print(s[-1])

-1 

s= 'Python is object oriented'
print(s[::-1])

detneiro tcejbo si nohtyP

s= 'Python is object oriented'
print(s[:-1])

Python is object oriente

s= 'Python is object oriented'
print(s[1:1])

s= 'Python is object oriented'
print(s[4:10])

on is 
---------------------------------------------------------------------------------------------------

s= ‘’
print(s[1])

invalid character in identifier

------------------------------------------------------------------------------------------------
S=‘Gaurav’
print(s[1])

name s is not defined 
-----------------------------------------------------------------------------------------------

s='a b cd'
print(len(s))
print(s[::2])
print(len(s[::2]))

6
abc
3
-----------------------------------------------------------------
s='a#b#c#d#'
print(s.split())
print(s.split('#'))
l=s.split('#')
s='$'.join(l)
print(s)


['a#b#c#d#']
['a', 'b', 'c', 'd', '']
a$b$c$d$
----------------------------------------------------------

S='Gaurav'
S=S[::-2][::-2]
print(S)

av
----------------------------------------------------------------
print(1>2)

false

--------------------------------------------------------
print(4%2, 5%2, 2%5, sep=‘, ’)

0 1 2
=----------------------------------------------------------------

s='abcba'
s.upper()
print(s)
print(s.count('A'), end = ',')
print(s.count('A', 2,4) , end = ',')
print(s.count('a', 2,4) , end = ',')

abcba
0,0,0
--------------------------------------------------

s = 'Aishwarya is python learner'
print(s.replace(" ", ""))

Aishwaryaispythonlearner
=----------------------------------------------------------------------------------------------------

s= dir(str)
print(s)


['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']



--------------------------------------------------------------------------------------------------------------

s= dir(str)
l = " "
fnd= l.join(s)
print(fnd.find("rstrip"))

---------------------------------------------------------------------------

s = input()
print(s.replace(" ", '\n'))

Aishwarya is a python learner 
Aishwarya
is
a
python
learner
---------------------------------------------------------------

s = input()   # read first and last name seperated by space 
first_name = s.split()[0]
last_name = s.split()[1]
print(first_name, len(first_name))
print(last_name , len(last_name))

-----------------------------------------------------------------
s= input()
l= len(s)//2
print(s[:l])
if len(s)%2==0 :
    print(s[l:])
else:
        print(s[l+1:])




---------------------------------------------------------------------------------------------------------------------------


s= """*****\t\t\t *   *\t\t\t----------|\n  *\t\t\t ** **\t\t\t |        |\n  *\t\t\t * * *\t\t\t o        |\n  *\t\t\t *   *\t\t\t/|\       |\n  *\t\t\t      \t\t\t/|\       |\n\t\t\t\t\t\t----------|"""
print(s)


