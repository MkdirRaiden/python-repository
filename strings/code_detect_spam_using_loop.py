spam_word=["make lot of money", "click here", "buy now", "subscribe"]
email=input("Enter your mail: ")
for item in spam_word:
    if item in email:
        print("spam")
else:
    print("none")      