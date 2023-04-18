print("Enter mode of operation\n1: addition\n2: subtraction\n3: multiplication\n4: division")
def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def mul(a, b):
    return a*b
def div(a, b):
    return a/b
sel = int(input("Enter mode of operation: "))
if sel==1:
    a, b=[int(x) for x in input("Enter the numbers: ").split()]
    print(f"The sum of {a}+{b} is: ", add(a, b))     
elif sel==2:
    a, b=[int(x) for x in input("Enter the numbers: ").split()]
    print(f"The subtraction of {a}-{b} is: ", sub(a, b))
elif sel==3:
    a, b=[int(x) for x in input("Enter the numbers: ").split()]
    print(f"The multiplication of {a}X{b} is: ", mul(a, b))
elif sel==4:
    a, b=[int(x) for x in input("Enter the numbers: ").split()]
    print(f"The division of {a}%{b} is: ", div(a, b))
else:
    print("Invalid choice of operation")            

