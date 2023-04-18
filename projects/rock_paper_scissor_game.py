import random
def _pattern_(n):
    for i in range(n):
        for j in range(i):
            print(" ", end='')
        for j in range(2*(n-i)-1):
            print("*", end='')
        for j in range(i):
            print(" ", end='')
        print() 
    for i in range(2, n+1):
        for j in range(n-i):
            print(" ", end='')
        for j in range(2*i-1):
            print("*", end='')
        for j in range(n-i):
            print(" ", end='')    
        print()        
def win_lose(com, me):
    if com=="r" and me=="p":
        return True
    elif com=="p" and me=="s":
        return True
    elif com=="s" and me=="r":
        return True
    elif com==me:
        return None
    else:
        return False         
print("Please enter 'e' to quit")        
me=input('''Enter "r" for "rock", "p" for "paper" and "s" for "scissor" :''') 
while me!='e'and (me=="r" or me=="p"or me=="s"):         
    choice=("r", "p", "s")
    random_num=random.randint(0,2)
    com=choice[random_num] 
    result=win_lose(com, me)  
    if result is True:
        print("You won")
        print(f"computer chose {com} and you chose {me} ")
        me=input('''Enter "r" for "rock", "p" for "paper" and "s" for "scissor" :''') 
    elif result is None:
        print("Draw")
        me=input('''Enter "r" for "rock", "p" for "paper" and "s" for "scissor" :''') 
    else:
        print("Computer wins")
        print(f"computer chose {com} and you chose {me} ")
        me=input('''Enter "r" for "rock", "p" for "paper" and "s" for "scissor" :''')  
else:
    if me=="e":   
        print("You quit the game\t")
        _pattern_(9)
    else:
        print("Invalid choice\nPlease restart the game")            
         