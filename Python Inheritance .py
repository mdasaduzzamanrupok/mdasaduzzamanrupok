#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Python Inheritance

class Phone:
    
    def call(self):
        print("You can call.")
    def message(self):
        print("You can message.")
        
        
class Sumsung(Phone):  #inheritance
    
    def photo(self):
        print("You can take photo.")
        
s = Sumsung()
s.call()
s.message()
s.photo()


# In[ ]:




