#using loops
def palindrome(p):
    mid=len(p)//2
    start, last=0, len(p)-1
    flag=0
    while start<mid:
        if p[start]==p[last]:
            start+=1
            last-=1
        else:
            flag=1
            break
    if flag==0:
        print("it is palindrome.")
    else:
        print("it is not palindrome.")
my_string=input("enter a string: ")
palindrome(my_string)
#using loop for symmetrical
def symm(s):
    mid=len(s)//2
    start1=0
    if len(s)%2==0:
       start2=mid
    else:
        start2=mid+1       
    flag=0      
    while (start1<mid and start2<len(s)-1):
        if s[start1]==s[start2]:
            start1+=1
            start2+=1
        else:
            flag=1
    if flag ==0:
        print("it is symmetrical.")
    else:
        print("it is not symmetrical") 
my_string=input("enter a string: ")
symm(my_string)                            
