N = int(input())
arr = []
for i in range(N):
    command = input().split(' ')
    if command[0]=='insert':
        arr.insert(int(command[1]), int(command[-1]))
    elif command[0] == 'print':
        print(arr)
    elif command[0] == 'remove':
        arr.remove(int(command[-1]))
    elif command[0] == 'append':
        arr.append(int(command[-1]))
    elif command[0] == 'sort':
        arr.sort()
    elif command[0] == 'pop':
        arr.pop(int())
    else:
        arr.reverse() 