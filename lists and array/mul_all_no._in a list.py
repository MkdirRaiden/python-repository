lst=[1, 4, 5, 3, 6]
def mul(lst):
    m=1
    for x in lst:
        m=m*x
    return m 
print(mul(lst))  
#removing empty tuple or empty list from a list
lst=[2, 'a', [], [1,2], {3,4}, {}]
new_lst=[x for x in lst if x!=[] and x!={}]
print(new_lst)     
