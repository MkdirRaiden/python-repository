tple=() #empty tuple
t = (1,) #tuple with one element
lst=[2 , 4, 5]
tuple_1=(2, 4, 53, 'hey', ()) #packing of tuples
print(tuple_1[0])
print(tuple_1[2:])
print(tuple(lst))
a, *b, c= tuple_1 #unpacking of tuples
print(a, *b, c, sep='\n')
#tuples are immutable
del tple
tuple_1.index(4)
tuple_1.count('hey')
len(tuple_1)
tple=(2, 4, 5, 1, 3)
new_t=tple+tuple_1
print(new_t)
my_string='hello'
t1=tuple(my_string)
print(t1)
print(list(my_string))
#and many more as in lists except we cant change element in tuple like list but we can convert
#into list and back to tuple