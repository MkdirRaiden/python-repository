#Array are similar to lists, the only difference is its data types are of same type
from array import *
val = array('i', [1, 5, 3, 0])
print(val)
for i in range(len(val)):
    print(val[i], end=' ')
#since array are similar to list hence all other methods of lists are also applicaple to an array
print(val.buffer_info())
arr = array('u', ['h', 'e', 'l', 'l', 'o'])
print(arr.buffer_info())
print(arr)
for x in arr:
    print(x, sep=' ')
new_arr = array(arr.typecode, ['i', 'j', 'k'])
print(new_arr) 
#some other operations
arr.append('k')
arr.extend(['g', 'k'])
print(arr) 
#etc  