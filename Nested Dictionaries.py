#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Nested Dictionaries

myfamily = { 

    "child1": { 
        
        "name": "Emily",
        "year": "2001"
        
    },
    "child2": {
        
        "name": "Clark",
        "year": "1999"
    },
    
    "child3": {
        
        "name": "Brainstron",
        "year": "2000"
        
    } 

}


# In[4]:


print(myfamily)


# In[5]:


#Create three dictionaries, then create one dictionary that will contain the other three dictionaries:

child4 = {
  "name" : "Emil",
  "year" : 2004
}
child5 = {
  "name" : "Tobias",
  "year" : 2007
}
child6 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily1 = {
  "child4" : child4,
  "child5" : child5,
  "child6" : child6
}


# In[6]:


print(myfamily1)


# In[7]:


print(myfamily1["child5"]["name"])


# In[ ]:




