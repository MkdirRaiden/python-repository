val = []
n = int(input())
for i in range(n):
    name = input()
    marks = float(input())
    val.append([name, marks])
val.sort(key=lambda x: x[1])
tem = val[1]
sec = tem[1]
names = []
for x in val:
    if x[1]==sec:
        names.append(x)
    else:
        continue    
names.sort(key=lambda x: x[0])
for name, mark in names:
    print(name, sep='\n')             
