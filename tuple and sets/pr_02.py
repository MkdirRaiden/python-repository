mat = [[10, 25, 20, 40],
      [15, 45, 35, 30],
      [24, 29, 37, 48],
      [32, 33, 39, 50]]
def func(mat):      
    val=[]      
    for item in mat:
        val1=val
        for element in item:
            val1.append(element)
    return val
my_list=func(mat)
my_list.sort()
k=int(input("Enter the value of k: "))
print(f"The {k}th smallest element is: ", my_list[k-1])            
