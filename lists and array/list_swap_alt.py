def swap(lst, p1, p2):
    get=lst[p1], lst[p2]
    lst[p2], lst[p1]=get
    return lst
lst=[1, 2, 6, 23, 'as', 'ghj']    
print(swap(lst, 2, 4))    

