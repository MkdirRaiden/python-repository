sentence=input("Enter your username: ")
if len(sentence)<10:
    print("Username contains less than 10 characters")
else:
    print("Username contains", len(sentence), "characters")