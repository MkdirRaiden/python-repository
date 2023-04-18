def _pattern_(n):
    for i in range(n-1):
        for j in range(i):
            print(" ", end='')
        for j in range(2*(n-i)-1):
            print("*", end='')
        for j in range(i):
            print(" ", end='')
        print() 
    for i in range(1, n+1):
        for j in range(n-i):
            print(" ", end='')
        for j in range(2*i-1):
            print("*", end='')
        for j in range(n-i):
            print(" ", end='')    
        print()
_pattern_(int(input('Enter a number: ')))        