#!/usr/bin/env python
# coding: utf-8

# In[1]:


def count_case(s):
    d = {"Uppercase characters": 0, "Lowercase characters": 0 } # dict. to store the counts 
   
    for i in s:
        if i.islower():
            d["Uppercase characters"]+=1
        elif i.isupper():
            d["Lowercase characters"]+=1
    return d


x = "hello how are YOU"


# In[2]:


count_case(x)


# In[ ]:




