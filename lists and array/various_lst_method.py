lst1=[1, 5, 6, 4]
lst2=['s', 'hey', 4, 23]
print(dict(zip(lst1, lst2))) #two list in key value pairs
print(lst1.count(1))
#lists cannot be subtracted but we can convert it into set and then do the sub.
print(set(lst1).difference(set(lst2)))
print(set(lst2).intersection(set(lst1)))
#flattaning a nested list
lst=[[1, 2, 4], [12, 4, 3], ['a', 'b'], [0]]
f_lst=[x for i in lst for x in i]
print(f_lst)