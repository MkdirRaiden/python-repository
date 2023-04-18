from functools import reduce
import copy
lst=['1', '2', '3','4']
new_list=list(map(lambda x: int(x), lst))
c_list=copy.deepcopy(new_list)
print(new_list)
n_list=list(map(lambda x: x*x, new_list))
f_list=list(filter(lambda x: x>5, n_list))
val=reduce(lambda x, y: x+y, f_list)
print(n_list, f_list, val)
print(c_list)
rev=c_list.sort(key=lambda x: x>2)
print(rev)