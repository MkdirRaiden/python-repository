def is_prime(y):
    prime_list=[]
    for i in range(y+1):
        if i==0 or i==1:
            continue
        else:
            div=0
            for j in range(2, (i//2)+1):
                if i%j==0:
                    div+=1
            if div==0:
                prime_list.append(i)
    return prime_list
y=int(input("Enter the upper bound: "))
lst=is_prime(y)
if len(lst)==0:
    print("there are no prime numbers in this range")
else:
    print("The list of prime numbers in this range are", lst)                        
