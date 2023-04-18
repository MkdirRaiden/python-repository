#list comprehension of set of coordinates of a cuboid
x=int(input())
y=int(input())
z=int(input())
n=int(input())
my_lst=[[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k!=n]
print(my_lst)