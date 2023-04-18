import sys
# initializing a with range()
a = range(1,10000)  #returns a list
# initializing a with xrange()
x = range(1,10000)  #returns xrange objects xrange is not supported in python 3
# testing the size of a
# range() takes more memory
print ("The size allotted using range() is : ")
print (sys.getsizeof(a))
# testing the size of x
# xrange() takes less memory
print ("The size allotted using xrange() is : ")
print (sys.getsizeof(x))