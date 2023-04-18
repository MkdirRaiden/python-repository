s=set() #empty set
l=[1,1,2,3,5,7,5]
s2=set(l)
t=(2,5,5,3,2,1)
s3=set(t)
my_string='hello'
s4=set(my_string)
s5={3,4,3,4,6,7,6}
print(s, l, s2, t, s3, s4, s5, sep='\n')
s.add(5)
print(s)
s.add(t) #adding tuple as a element as it is hashable
print(s)
print(s.add(7)) #will show error as list cant be added as a element
s.update(s4)
s.update(l)
print(s)
s.union(s2)
s.intersection(s2)
s.difference(s2)
s.remove(5) #will show error if element is not present in s
s.discard(5) #will do nothing if element is not present
s.pop() 
s.isdisjoint(s2)
s.issubset(s2)
s.issuperset(s3)
s.difference_update(s2)
#and many more
