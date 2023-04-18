def checkleap(year):
    if (year%400==0) or (year%4==0 and year%100!=0):
        return True
    else: 
        return False  
if checkleap(year=int(input("Enter a year: "))) is True:
    print("Leap year") 
else:
    print("Not a leap year")             