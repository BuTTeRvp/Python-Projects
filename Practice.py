l1 = [2,4,3]
 
l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.



l1_r = list(map(lambda x : str(x), l1[::-1]))                         #list[::-1] 
l2_r = list(map(lambda x : str(x), l2[::-1]))

def int_str(x): 
    empty_string = ""          # takes ints from a list and concantiates them in a string 
    for i in x:
        empty_string += i
    return int(empty_string)
x = int_str(l1_r)
y = int_str(l2_r)
z = str(x + y)
print(list(map(lambda x : int(x), z[::-1])))
