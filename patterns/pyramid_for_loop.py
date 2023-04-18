n=int(input("Enter the value of n: "))
i=1
while i<=n:
    for j in range(n-i):
        print(" ", end="")
    for j in range((2*i)-1):
        print("*", end="")
    for j in range(n-i):
        print(" ", end="")
    i+=1
    print()

