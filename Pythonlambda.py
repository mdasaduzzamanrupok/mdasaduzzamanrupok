#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#lambda function
#A lambda function is a small anonymous function.


# In[1]:


x = lambda a: a + 10
print(x(5))


# In[2]:


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))


# In[3]:


x = lambda a, b, c: a + b + c
print(x(5, 6, 2))


# In[4]:


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11)) 
print(mytripler(11))


# In[ ]:




