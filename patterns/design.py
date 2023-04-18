N, M = map(int, input().split(' '))
mid = (N+1)//2
for i in range(1, mid+1):
    if i == mid:
        print('WELCOME'.center(3*N, '-')) 
    else:    
        for j in range(mid-i):
            print('---', end='')
        for j in range((2*i)-1):
            print('.|.', end='')
        for j in range(mid-i):
            print('---', end='')
        print()          
for i in range(mid):
    if i==0:
        continue
    else:
        for j in range(i):
            print('---', end='')
        for j in range(2*(mid-i)-1):
            print('.|.', end='')
        for j in range(i):
            print('---', end='')
        print()    
        