def remove_nth(lst):
    my_list=[]
    for i in range(len(lst)):
        if lst[i] in my_list:
            continue
        else:
            tem_ind=[]
            count=1
            for j in range(len(lst)):
                if j==i:
                    continue
                else:
                    if lst[i]==lst[j]:       
                        count+=1
                        tem_ind.append(j)
        my_list.append(lst[i])
        if count>1:
            print(f"{lst[i]} occured {count} times at indexes {i} first and other {tem_ind} indexes")  
lst=[1, 1, 2, 4, 5, 6, 3, 2, 1, 1, 2, 6, 5]
remove_nth(lst)
n=input("Enter index of value to be deleted: ")
while n!='e':
    lst.pop(int(n))
    print("Updated list: ", lst)
    n=input("Enter index of value to be deleted or enter 'e' to exit: ")
else:
    print("Updated list", lst)
