from functools import reduce
lst=[100, 2 ,5, 7, 34, 0, -4, -37]
def func1(a):
    return True if a>0 else False
fil_lst=[x for x in filter(func1, lst)]
print(fil_lst) 
def mul_5(a):
    return a*5
mul_lst=[x for x in map(mul_5, fil_lst)] 
print(mul_lst)
dic={i:j for i in mul_lst for j in range(5)}
print(dic)      
def sub(a, b):
    return a-b
print(reduce(sub, mul_lst))   
