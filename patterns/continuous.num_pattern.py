
def contnum(n):
    num = 1
    for i in range(n):
        for j in range(i+1):
            print(num, end=" ")
            num = num + 1
        print("\r")
 
n = 5
contnum(n)