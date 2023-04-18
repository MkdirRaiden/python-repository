#** is used for dictionary
def func(a, b, c):
    print(a, b, c)
d = {'a':4, 'b':'hi', 'c': 'r'}
func(**d)  

# A Python program to demonstrate packing of
# dictionary items using **
def fun(**kwargs):
    for key in kwargs:
        print("%s = %s" % (key, kwargs[key]))
# Driver code
fun(name="Muktadir", ID="01", language="Python")
