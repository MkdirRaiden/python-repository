n=int(input("enter the value of n: "))
for i in range(n):
    for j in range(n-i):
        print(" ", end='')
    for j in range((2*i)-1):
        print("*", end='')
    for j in range(n-i):
        print(" ", end ='')
    print()



