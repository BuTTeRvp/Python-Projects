#!/usr/bin/env python
# coding: utf-8

# In[ ]:



list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1),]
list2 = []
l3 = []
for i in list:       #reverse the tuples
    i = i[::-1]
    list2.append(i)
    
list2.sort()         #reverse = sort  = sorted in increasing order by the last element in each tuple
                     

for i in list2:      # expected O/P
    i = i[::-1]
    l3.append(i)
print(l3)  

