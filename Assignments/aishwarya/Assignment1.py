predict below prog output 
s1 = 'GAURAV'
s2 = 'Tuteur.py@gmail.com'
print(len(s1),len(s2))


6,19

---------------------------------------------------------------------------------
Read input from user and print its length 


a = input()  #read input from user 
print( "input is" ,a, len(a))

---------------------------------------------------------------------------------
WAP to input 2 number and print their sum and diff


a = input()  #read input 1 from user 
b= input()  #read input 2 from user 
print(int(a) + int(b))  # addition of 2 numbers 
print(int(a) - int(b))   # subtarction of 2 numbers 

-------------------------------------------------------------------------------------

predict output 
s1= 'ab'
s2= 'de'
s3 = s1 + s2
print(s3)

abde

-------------------------------------------------------------------------------------


s1 = 'ab'*4
print(s1)

abababab
----------------------------------------------------------------------------------
predict output
s1 = 'ab\n'*4
print(s1)

ab
ab
ab
ab
-------------------------------------------------------------------------------------

a = input()
n = input()
print ((a +'\n')*int(n))



-----------------------------------------------------------------------------------

predict output

res = print('Gaurav')
print(res)

Gaurav
None

----------------------------------------------------------------------------------

res = len('tutrur.py@gmail.com')
print(type(res))


int
-------------------------------------------------------------------------------------

s1 = 'gaurav'
s2 = 'tutrur.py@gmail.com'
s3 = s1 + '\n'+  s2 
print(type(s3))
print(len(s3))


str
26

---------------------------------------------------------------------------
Find the name of function to find the square root. (see all the options available in dir() of math)
sqrt

---------------------------------------------------------------------------------
WAP to input a number and print its square root ().


n = input()  # read number 
print(math.sqrt(int(n)))

-------------------------------------------------------------------------------

WAP to input 4 numbers from user and print their average

n1 = input() 
n2 = input() 
n3 = input()
n4 = input()
n = (int(n1)+int(n2)+int(n3)+int(n4))/4
print("avergae of 4 number is" , n)
------------------------------------------------------------------------------------
print(_name_) in interpretor 

__main__

=-----------------------------------------

print(_name_) in script

__main__

---------------------------------------------

print(__builtins__.__name__)

builtins

------------------------------------------
print(int.__name__)