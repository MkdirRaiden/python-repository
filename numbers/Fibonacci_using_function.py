def _fibonacci_(n):
    a,b=0, 1
    sum=0
    for i in range(n):
        print(a, end=" ")
        sum=a+b
        a=b
        b=sum
_fibonacci_(n=int(input("Enter the value of n: ")))  