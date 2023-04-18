#sort a tuple by 2nd item
from pstats import SortKey

tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
lst1 = sorted(tuple1, key=lambda x: x[1])
print(tuple(lst1))
lst = [[3,2], [2], [4,9], [1, 0]]
lst2 = sorted(lst, key=lambda x:x[0])
print(lst2)  
lst.sort(key=lambda x: x[0])
print(lst)
mix = [1, 'a', 'b', 7, 4, 8, 3]
n_mix = [x for x in filter(lambda x: x if type(x) is int else None, mix )]
print(sorted(n_mix))