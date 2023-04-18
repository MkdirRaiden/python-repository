lst=[]
count = 1
while count<=4:
    a= int(input("Enter a number: "))
    lst.append(a)
    count+=1
lst.sort()
print("The greatest number is: ", lst[3])    
