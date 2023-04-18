n=int(input("enter a number: ")) # taking input from user
for i in range(1, n+1):
    for j in range(n-i):
        print(' ', end='')
    for j in range(2*i-1):
        print('*', end='')
    for j in range(n-i):
        print(' ',end='')
    print()            