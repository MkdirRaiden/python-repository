val = [1, 2, 2, 2, 3, 3,]
val1 = [5, 6, 'hey', 'hi']
d= {k:[] for k in val}
print(list(zip(val, val1)))
print(d)
for key, value in zip(val, val1):
    d[key].append(value)
print(d)    