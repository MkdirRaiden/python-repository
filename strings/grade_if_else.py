mark=int(input("Please enter your mark: "))
if mark in range(90, 100):
    print("Your grade is E")
elif mark in range(70, 80):
    print("Your grade is A")
elif mark in range(60, 70):
    print("Your grade is B")
elif mark in range(50, 60):
    print("Your grade is C")
else:
    print ("your grade is F")

