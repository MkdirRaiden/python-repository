size = int(input("Enter the value of size: "))
val = [chr(x).lower() for x in range(65, 65+26)]
width = 4*size-3
lst = []
for i in range(size):
    if i == size-1:
        lst.append(val[size-1].center(width, '-'))
    else:
        lst.append('-'.join(val[i:size][::-1]+val[i+1:size]).center(width, '-'))
print('\n'.join(reversed(lst)))
print('\n'.join(lst[1:]))           