#!/usr/bin/env python
# coding: utf-8

# In[4]:


#reverse a string

# A1 --> Lambda

x = input("Enter a string to reverse : ")

reverse = lambda x: x[::-1]

print(reverse(x))


# In[3]:


#A2 --> Normal function


inpu = input("Enter a string to reverse : ")

def fun_reverse(x):
    x = x[::-1]
    return x

print(fun_reverse(inpu))


# In[ ]:





# In[ ]:




