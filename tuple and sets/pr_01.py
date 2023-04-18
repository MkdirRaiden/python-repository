mat = [[0, 1, 0, 0, 1],
       [1, 0, 1, 1, 0],
       [0, 1, 0, 0, 1],
       [1, 1, 1, 0, 0]]
tup_mat=[x for x in map(lambda x:tuple(x), mat)]       
set_mat=set(tup_mat)
for item in set_mat:
    print(item, end='\n')