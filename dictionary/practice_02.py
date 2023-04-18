lis1 = ['a', 'a', 2, 4]
lis2 = ['a', 'b', 'hey']
z = zip(lis1, lis2)
dic = {k:v for k, v in z}
print(dic)