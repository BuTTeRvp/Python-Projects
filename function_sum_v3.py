#!/usr/bin/env python
# coding: utf-8

# In[ ]:


num_of_num = input("Enter how many numbers to add :")  # User input
list_of_num = []                                         # empty list
i = 1
if num_of_num.isdigit():   
     while i <= int(num_of_num):
            num = input("Enter number: ")               #user input
            if num.isdigit() :
                list_of_num.append(int(num))            #user input -> Empty list
                i += 1
    
            else:
                print("Invalid Input")                 
                continue
else:
    print("Invalid Input")
    
    
def list_sum(list):                 # FUNCTION returns SUM OF ALL THE NUMBERS in a List.
    x = 0
    for i in list:
        x+=i

        
    return x


list_sum(list_of_num)


# In[ ]:




