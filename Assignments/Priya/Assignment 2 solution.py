
# coding: utf-8

# In[5]:


s='Python is Object Oriented' 
s[-1] 
 


# In[6]:


s='Python is Object Oriented'
s[::-1]


# In[17]:


s='Python is Object Oriented' 
s[1:1] 


# In[18]:


s='Python is Object Oriented' 
s[:-1]


# In[19]:


s='Python is Object Oriented'
s[4:10] 


# In[34]:


#What error do you see for following statements:
s= ''
print(s[1])


# In[40]:


#S=‘Gaurav’
#print(s[1]) : string index out of range, since we are trying to get a charecter from string 's' instead of string 'S'.

S='Gaurav'
print(S[1]) 


# In[41]:


s='a b cd'
print(len(s))
print(s[::2])
print(len(s[::2])) 


# In[44]:


s='a#b#c#d#'
print(s.split())
print(s.split('#'))
l=s.split('#')
s='$'.join(l)
print(s) 


# In[52]:


S='Gaurav'
S=S[::-2][::-2]
print(S) 


# In[53]:


print(1>2)


# In[58]:


print(4%2, 5%2, 2%5, sep=',' )


# In[67]:


s='abcba'
s.upper()
print(s.upper())
print(s.count('A'), end = ',')
print(s.count('A',2,4), end = ',')
print(s.count('a', 2,4), end = ',') 


# In[87]:


str1 = input('enter a string: ')
print(str1.replace(' ',''))


# In[85]:


#[] an empty string


# In[79]:


print(dir(str))


# In[81]:


if('rtrip' in 'str')
print(str)


# In[84]:


print("*****")
print("  *  ")
print("  *  ")
print("  *  ")
print("  *  ")


# In[88]:


str1 = input('enter a string: ')
print(str1.replace(' ','\n'))

