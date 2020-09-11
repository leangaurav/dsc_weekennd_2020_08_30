1. output:

s='python is oject oriented'
s[::-1]=>'detneiro tcejo si nohtyp'
s[:-1]=>'python is oject oriente'
S[1:1]=>''
s[4:10]=> 'on is '

2. Error:index error-> string index out of range

3.string index out of range

4. 
a)s='a b cd'
print(len(s))=> 6
print(s[::2])=> abc
print(len(s[::2]))=> 3

b)s='a#b#c#d#'
print(s.split())=>['a#b#c#d#']
print(s.split('#')) => ['a', 'b', 'c', 'd', '']
l=s.split('#')
s='$'.join(l)
print(s) =>a$b$c$d$

c)S='Gaurav'
S=S[::-2][::-2]=> av

d)print(1>2)=>False

e)print(4%2, 5%2, 2%5, sep=‘, ’)

f)s='abcba'
s.upper()
a=s.upper()
print(a)=>
print(s)=>abcd
print(a.count('A'),end=',') 
print(a.count('A',2,4),end=',')
print(s.count('a',2,4),end=',')  => ouput:ABCD
					  abcd
					  2,0,0

5) Program to remove white spaces:

s=input("enter the name")
a=s.replace(" ",'')
print(a)
   
6) [] => donote the list data-type in pyhton.

7) All methods(functions/operations) available in a string: print((dir(str)))

8) rstrip function in str
s='kishor'
print('rstrip' in dir(s)) => true

10) Progrm to input a string and replace all space with new lines (\n) and print again.
s=input("Enter the name")
a=s.replace(' ','\n')

11) Program to input complete name(first and last name separated by space) and print first and last
name separately along with their length in upper case.
s=input("Enter the name")
a=s.upper()
list =a.split(' ')
for i in list:
 print(i,end='')
 print(len(i))

12) Program to input a string and split it into 2 halves
s=input("Enter the string")
count=len(s)//2
print(s[:count])
print(s[count:])
