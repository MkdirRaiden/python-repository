def prin(*args):
    for i in args:
        print(i,end="\n")
def func(*args):
    args = list(args)
    args[0]= "Muktadir"
    args[1]= 26
    prin(*args)
func('Harry', 20, 'guwahati', 'student')    
