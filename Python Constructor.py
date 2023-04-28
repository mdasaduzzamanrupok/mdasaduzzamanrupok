#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Python Constructor

class Student:
    roll = ""
    gpa = ""
    
    #constructor
    def __init__(self, roll, gpa):
        self.roll = roll
        self.gpa  = gpa
    def display(self):
        print(f"Roll : {self.roll}, Gpa : {self.gpa}")

rupok = Student(108,3.52)
rupok.display()


# In[ ]:




