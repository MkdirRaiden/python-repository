def sum(n):
    if n<0:
        return None
    elif n==1:
        return 1
    else:
        return sum(n-1)+n
a =sum(n=int(input("Enter the value of n: ")))
print((a))
