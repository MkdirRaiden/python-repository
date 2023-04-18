lst1 = ['name', 'age', 'city', 'job']
lst2 = ['Muktadir', 26, 'guwahati', 'student']
dic = {x:y for x, y in zip(lst1, lst2)}
print(dic)
for key, value in dic.items():
    print(key, value, end='\n')
val= [(1, 2, 3), (3, 2, 1)]
for x, y , z in val:
    print(x, y, z, end='\n')    