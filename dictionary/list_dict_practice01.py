#convert lists into similar key value lists
list1=[1, 2, 2, 2, 3]
list2=['3', 3, 'hi', 'hello']
d={key:[] for key in list1}
for key, value in zip(list1, list2):
    d[key].append(value)
print(d)   
#convert each element of a list into a list of lists
lst= ['hi', 'hello', 4, 5]
new_lst=[]
for x in lst:
    new_lst.append([x])
print(new_lst)
t_lst=[x for x in list(map(lambda x: [x], lst))]  
print(tuple(t_lst))  
#converting a given list into a tree like dictionary
test_list= [[1], [2, 1], [3, 1], [4, 2, 1], [5, 2, 1], [6, 3, 1], [7, 3, 1]]
#output ={1: {2: {4: {}, 5: {}}, 3: {6: {}, 7: {}}}}
def form_tree(test_list):
    tree={}
    for item in test_list:
        tree2=tree
        for key in item[::-1]:
            if key not in tree2:
                tree2[key]={}
            tree2=tree2[key]
    return tree
print(form_tree(test_list))                


