def greet(name):
    print("hello", name)
greet('Muktadir')
def add(a, *b): # here b is tuple of multiple arguments
    return a+sum(b)
print('sum: ', add(5, 6, 3, 4, 3, 1))
def func(name, **b):#here b is dictionary of key=vlue pairs
    print(name, sep='\n')
    for i,j in b.items():
        print(i, j, end="\n")    
func('Muktadir Ahmed', age=26, city= 'Guwahati')    
        