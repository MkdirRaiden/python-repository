n=int(input("Enter the value of n: "))
_emptylist_=[]
for i in range(n):
    _emptylist_.append("*"*(i+1))
print("\n".join(_emptylist_))
