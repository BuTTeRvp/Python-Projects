#!/usr/bin/env python
# coding: utf-8

# In[3]:


#This function should add ALL the numbers present in any kind of list/tuple, will ignore 2d(nested) objects.
def list_sum(list):                 
    x = 0
    for i in list:
        if isinstance(i, (int, float)) :
             x = x + i
    return x



# example 
list =  ({'Hey': 11, 'there': 31, 'Vivek': 23}, [1000,1], 6, 7, 7, 8, 9,"a", "b","10000",10000.0)
list_sum(list)


# In[ ]:




