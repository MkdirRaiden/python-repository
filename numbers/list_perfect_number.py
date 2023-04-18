def is_perfect(num):
    list_div=[1]
    list_str=["1"]
    for i in range(2, (num//2)+1):
        if num%i==0:
            list_div.append(i)
            list_str.append(str(i))
    my_str="+".join(list_str)    
    if sum(list_div)==num:
        print(f"{num} is a perfect number as its div. sum i.e {my_str}={num}")
    else:
        print(f"{num} is a not perfect number as its div. sum i.e {my_str}={sum(list_div)}") 
is_perfect(int(input("Enter a number: ")))  
          


