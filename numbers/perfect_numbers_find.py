def perfect_numbers(n):
    list=[]
    for i in range(2, n+1):
        tem_list=[]
        for j in range(1, (i//2)+1):
            if i%j==0:
                tem_list.append(j)
        if sum(tem_list)==i:
            list.append(i)  
    return print("The list of perfect numbers are:", list)
perfect_numbers(int(input("Enter the value of upper bound: ")))