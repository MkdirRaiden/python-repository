#some methods of dictionary
d = {} #empty dictionary
d1 = {1:2, 3:4, 5:6, 4:{2:'a', 0:'hi'}}
print(d1[1])
d2 = d1.copy()
print(d2)
print(d1.keys(), d1.values())
print(d1.items())
d2.update({7:'hello'})
d2.update({1:'hey'})
print(d2)
d2.pop(3)
print(d2)
print(d2.get(0)) #this method dont throw error if not present
print(d2[4][0]) #throws error if key is not present in dic
print(d2.popitem()) #delete the last key-value pairs in a dic
d2.clear() #clears a dic
print(d2)
