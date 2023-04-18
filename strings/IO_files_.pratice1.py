import random
def game():
    score=random.randint(0, 100)
    print(f"The score is {score}")
    return score
score=game()
with open("highscore.txt", "r") as f:
    hiscore=int(f.read())
if (hiscore<score):
    with open("highscore.txt", "w") as f:
        f.write(str(score))
               
    