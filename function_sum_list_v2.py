



#This function should add ALL the numbers (int,float) present in any kind of list/tuple, will ignore nested(2d) objects.
def list_sum(list):                 
    x = 0
    for i in list:
        if isinstance(i, (int, float))  :
             x = x + i
    return x



list =  ({'Hey': 11, 'there': 31, 'Vivek': 23}, [1000,1], 6, 7, 7, 8, 9,"a", "b","10000",6.0)

list_sum(list)












