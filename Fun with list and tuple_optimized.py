#!/usr/bin/env python
# coding: utf-8

# In[ ]:


list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1),]
listx= [i[::-1] for i in list]

listx.sort()
listy= [i[::-1] for i in listx]
print(listy)

