#check a string is symmetrical or palindrome
#if first half of a string is same as the second half it is called symmetrical e.g. potpot
#if first half and second half read from reverse is same e.g. # pottop it is palindrome
#using slicing method
def is_palindrome(p):
    rev_p=p[::-1]
    n=len(p)
    if n%2==0:
        if p[:n//2]==rev_p[:n//2]:
            print(f"{p} is palindrome.")
        else:
            print(f"{p} is not palindrome.")
    else:
        if p[:(n+1)//2]==rev_p[:(n+1)//2]:
            print("It is palindrome.")
        else:
            print("it is not palindrome.")    
my_string=input("Enter a string: ")
is_palindrome(my_string)                    
def is_symmetrical(s):
    n=len(s)
    if n%2==0:
        if s[:n//2]==s[n//2:]:
            print(f"{s} is symmetrical.")
        else:
            print(f"{s} is not symmetrical.")
    else:
        if s[:(n+1)//2]==s[((n+1)//2)+1:]:
            print("It is symmetrical.")
        else:
            print("It is not symmetrical")    
my_string=input("Enter a string: ")
is_symmetrical(my_string) 