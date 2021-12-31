#!/usr/bin/env python
# coding: utf-8

# In[7]:


def count_case(s):
    d = {"Uppercase characters": 0, "Lowercase characters": 0 } # dict. to store the counts 
   
    for i in s:
        if i.islower():
            d["Lowercase characters"]+=1
        elif i.isupper():
            d["Uppercase characters"]+=1
    return d


x =  'The quick Brow Fox'


# In[8]:


count_case(x)


# In[ ]:




