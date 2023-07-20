#!/usr/bin/env python
# coding: utf-8

# In[12]:


#string formating

price = 41

order = "Banana price is {} dollers"

print(order.format(price))


# In[11]:


price = 56 

txt = "Fish price is {:.2f} Dollers"

print(txt.format(price))


# In[15]:


quantity = 3 

item = 500

price = 47

ourorder = "I want {} Pices of item number {} for {:.2f} dollers" 

print(ourorder.format(quantity, item, price))


# In[20]:


myoder = "I have a {carname}, it is a {model}"

print(myorder.format(carname= "ford", model = "Musting"))


# In[ ]:


m

