Input temperature in Fahrenheit in print in Celsius.

f = input() # take temp in fahrenheit
c = int(f)*1.8 + 32
print(c)  

----------------------------------------------------------------------------------------
Write a program to input a number and print its square and cube.

n= input()
print('sqrt of n is',  int(n)**0.5)
print('cube of n is ', int(n)**3)
-----------------------------------------------------------------------------------------
WAP to input a number n and a number m and print the result of following

n = input()
m= input()
print(int(m)**2 + int(n)**2)

--------------------------------------------------------------------------------

m = input()
n= input()

print(int(m)**int(n))
print(pow(int(m),int(n)))

=-----------------------------------------------------------------------

Simple interest calculator

P = input() # principal amount
r = input() # trate
t= input() #time
I = int(P)*int(r)*int(t)/100
print('interest is', I )

---------------------------------------------------------------------------
sum of n natural number 

n = input()
sum1 = int(n)*(int(n)+1)/2
print('sum of', n ,'natural number is' , sum1)
--------------------------------------------------------------------------

swap 2 number in 3 way 

a = input()
b = input()
c  = a
a = b 
b = c
print(a ,b)




a = input()
b = input()
a = int(a)+int(b)
b= int(a)-int(b)
a = a-b

print(a ,b)

----------------------------------------------------------------------

chr = input() 
print('ascii value of ', chr, 'is', ord(chr)) 


-------------------------------------------------------------------------

area = input() #area of circle 
r = (int(area)/3.14)**0.5
print('radius of circle is ' , r)
print('circumference of circle is ', 2*r)
------------------------------------------------------------------------------

# input 5 subject marks 
sub1 = input()
sub2 = input()
sub3 = input()
sub4 = input()
sub5 = input()
sum = int(sub1)+int(sub2)+int(sub3)+int(sub4)+int(sub5)
percent = sum*100/500
print('total % of student is ', percent)