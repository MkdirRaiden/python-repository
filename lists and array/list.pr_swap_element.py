#swapping first and last element in a list
my_list=[1, 4, 7, 13, 16, 3, 55, 87]
def swap(my_list):
    tem=my_list[0]
    my_list[0]=my_list[-1]
    my_list[-1]=tem
    return print(my_list)
swap(my_list)
#swapping mid elements with first and last element in a list
my_list=[3, 4, 2, 5, 4, 24, 54, 'as', 'adg', 'hey', 'hello']
def swapping(my_list):
    l=len(my_list)
    if l%2==0:
        mid1, mid2=l//2, (l//2)+1
        my_list[mid1-1:mid2]=[my_list[0], my_list[-1]]
    else:
        mid=(l+1)//2
        my_list[mid-1:mid]=[my_list[0], my_list[-1]]
    return print(my_list)
swapping(my_list)  
#packing and unpacking approach of the above problem
my_list=[3, 4, 'a', 'b', 'abc']
def swap(my_list):
    a, *b, c= my_list
    my_list=[c, *b, a]
    return print(my_list) 
swap(my_list)
         




