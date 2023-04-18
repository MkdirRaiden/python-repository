import copy
mlst=[1, 2, "a", "b"]
lst=copy.deepcopy(mlst)
print(reversed(lst))
print(mlst.count('a'))
tple=tuple(("hello", "world"))
lst[2:4]=[3, 4, 5]
print(lst)
lst.extend(tple)
print(lst)
lst.insert(5, "Its" )
print(lst)
lst.pop(5)
print(lst)
print(lst.pop())
lst.append("world")
print(lst)
lst.remove(5)
print(lst)
del lst[4:]
print(lst)
for i in range(len(lst)):
    print(lst[i])
lst.clear()
print(lst)
del lst    