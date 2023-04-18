#Using list comprehension 
import copy
lst=['agh', 'hgl', 'hello']
Lst=copy.deepcopy(lst)
new_lst=[x.replace('a', 'A').replace('_', ' ').replace('l', 'T') for x in Lst]
print(new_lst)
#Using naive method
my_string=' '.join(Lst)
new_string=my_string.replace('a', 'B').replace('o', 's')
print(new_string.split(' '))
print(lst)
