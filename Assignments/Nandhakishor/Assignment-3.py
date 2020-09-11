1) Fahrenheit  -> celcious

f=float(input("Enter the Fahrenheit temperature"))
c=(f-32)*5/9
print("The temperature is: ",c,' in celcious')

2. Square and cube of number:

a=int(input("Enter the number"))
print("The square is:", a*a)
print("The cube is:", a*a*a)

3. n2 + m2 

n=int(input("Enter the number n"))
m=int(input("Enter the number m"))
print("The result: ",(n*n)+(m*m))

4. n**m
n=int(input("Enter the base"))
m=int(input("Enter the power"))
print("The Result1 is ", n**m)
print("The Result2 is ", pow(n,m))

5.S.I

p=int(input("Enter the principle"))
n=int(input("Enter the no.of years"))
r=int(input("Enter the rate of interest"))
print("The simple interest is: ",(p*n*r)/100)

6. C.I

p=int(input("Enter the principle"))
t=int(input("Enter the time span"))
r=int(input("Enter the rate of interest"))
CI=p*pow((1+(r/100)),t)
print("The compound interest is: ", CI)

7. program to find sum of n natural numbers

n=int(input("Enter the value"))
temp=0
if n<=0:
 print("Enter the positive value")
else:
    for n in range(1,n+1,1):
      temp=temp+n
    print("The sum of first ",n," natural number is",temp)
    
8. Swap without temp

a=4
b=6
a,b=b,a
print(a,b)

With temp:

a=4
b=6
temp=b
b=a
a=temp
print(a,b)

9. ASCII Value of character:

a=input("Enter the character")
print(ord(a))

10. ASCII value of white space:
a=input("Enter the character")
print(ord(a))

11. circumference an area of circle
import math
area=int(input("Enter the area of circle"))
r=math.sqrt(area/3.14)
print("The radius is ",r,"The circumference is ",2*3.144*r)

12. Print percent of 5 subjects

M1=int(input("Enter mark 1"))
M2=int(input("Enter mark 2"))
M3=int(input("Enter mark 3"))
M4=int(input("Enter mark 4"))
M5=int(input("Enter mark 5"))
PER=((M1+M2+M3+M4+M5)/500)*100
print("The percentge value is ",PER)