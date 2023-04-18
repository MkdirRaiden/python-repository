size = int(input("Enter a number: "))
val = [chr(x).lower() for x in range(65, 65+26)]
width = 4*size-3
for i in range(size):
    if i == 0:
        print(val[size-1].center(width, '-'))
    else:
        print('-'.join([x for x in reversed(val[size-i:size])]+[x for x in val[(size-i)-1:size]]).center(width, '-'), end='')
        print()
for i in range(size):
    if i == 0:
        continue
    elif i == size-1:
        print(val[size-1].center(width, '-'))
    else:
        print('-'.join([x for x in reversed(val[i:size])]+[x for x in val[i+1:size]]).center(width, '-'), end='')
        print()