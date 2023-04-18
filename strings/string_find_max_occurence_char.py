text=input("Enter your messages: ")
i=0
lst1=[]
lst2=[]
while i<len(text):
    rep=text.count(text[i])
    lst1.append(rep) 
    lst2.append(text[i])
    i+=1
f=lst1.index(max(lst1))
print(f" '{lst2[f]}' is present highest number of times and it occured {max(lst1)} times. ")