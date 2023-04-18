Marks=[]
count=1
while count<=6:
    mark=int(input("Enter marks obtained in every subjects: "))
    Marks.append(mark)
    count+=1
Marks.sort()
if Marks[0]<33:
    print("Sorry! you failed in your individual subject.")
else:
    if sum(Marks)>=(40/100)*600:
        print("Congrats! you passed")
    else:
        print("Sorry! you failed in overall percentile")



    
