def func(lst):
    dic={}
    for i in range(len(lst)):
        v=lst.count(lst[i])
        k=lst[i]
        dic.update({k:v})
    return dic
lst=[2, 3, 2, 4,'hey', 'hi','hi','hey', 'hi', 7, 7, 2, 8]
print(func(lst)) 
lst=list(range(1, 100))
print(any(i%2==0 for i in lst))
print(all(i>0 for i in lst))       