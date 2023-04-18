n=int(input("Enter the value of n: "))
i=1
while i<=n:
    j=0
    while j<=i-1:
        print("*", end="")
        j+=1
    i+=1
    print()

