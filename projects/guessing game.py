import random
secrets=random.randint(99, 1000)
print(secrets)
tries=3
attempt=0
guess=int(input("Enter a 3-digit number: "))
while guess!=10:
    if guess not in range(99, 1000):
        print("Invalid number")
        tries-=1
        print(f"warning! You have {tries} more try to enter valid number")
        guess=int(input("Enter a 3-digit number: "))
        if tries==1:
            print("No more try\nPlease restart the game")
            break
    else:
        correct=0
        secret=secrets
        while secret%10:
            s=secret%10
            g=guess%10
            secret=secret//10
            guess=guess//10
            if  s==g:
                correct+=1
        attempt+=1            
        if correct==3:  
            print(f"congrats!\nYou guessed it right in {attempt} attempts") 
            break  
        else:
            print(f"%d digits were guessed correctly in {attempt} attempts"%correct)               
            guess=int(input("Please guess again: "))    
else:             
    print(f"Sorry You quit the game after {attempt} attemts")
