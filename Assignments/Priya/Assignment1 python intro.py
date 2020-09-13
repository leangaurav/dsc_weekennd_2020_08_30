
# coding: utf-8

# In[1]:


s1= 'Gaurav'
s2= 'tuteur.py@gmail.com'
print (len(s1), len(s2))


# In[2]:


a= input('Enter a string: ')
print (len(a))  


# In[3]:


a= int(input('Enter 1st number: '))
b= int(input('Enter 2st number: '))
print ("Sum of 1st and 2nd number is", a+b)
print ("Difference of 1st and 2nd number is", a-b)


# In[4]:


s1 = 'ab'
s2 = 'de'
s3 = s1 + s2
print(s3)


# In[5]:


s1 = 'ab'*4
print (s1)


# In[6]:


s1 = 'ab\n'*4
print (s1)


# In[7]:


a= input('Enter a string: ')
n=int(input('Enter a number: '))
print((a + '\n')*n)


# In[8]:


res = print('Gaurav')
print(res)


# In[9]:


res = len('tuteur.py@gmail.com')
print(type(res))


# In[10]:


s1 ='Gaurarv'
s2 ='tuteur.py@gmail.com'
s3 = s1 + '\n' + s2
print(type(s3))
print(len(s3))


# In[11]:


#12. Find the name of function to find the square root. 
#(see all the options available in dir() of math)

import math
print(dir(math))


# In[12]:


#WAP to input a number and print its square root ().

a= int(input('Enter a number: '))
print('the square root of {} is:'.format(a),math.sqrt(a)) 


# In[14]:


#WAP to input 4 numbers from user and print their average

lst = eval(input("Enter a list: "))
print('the average of {} is = '.format(lst), sum(lst)/len(lst))


# In[1]:


help(abs)


# In[2]:


print(__name__)


# In[4]:


#18. Does the dir of int class contain an attribute __name__ (Y/N) ----->No

print(dir(int))


# In[5]:


print (__name__)
print (__builtins__.__name__)
print (int.__name__)


