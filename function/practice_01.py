def func(a, b, c, d):
    print(a, b, c, d)
val = [4, 'hi', 0, 2] #if we want to pass this list as arguments
func(*val) # this is called unpackting 
#note the elements in the val must be of same in numbers as the no. of arguments
# This function uses packing to sum
# unknown number of arguments
def mySum(*args):
    return sum(args) 
# Driver code
val1= [3, 4, 5, 5]
print(mySum(1, 2, 3, 4, 5))
print(mySum(10, 20))
print(mySum(*val1))
