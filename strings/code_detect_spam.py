spam_word=["make lot of money", "click here", "buy now", "subscribe"]
email=input("Enter your mail: ")
spam=False
if "make a lot of money" in email:
   spam=True
elif 'click here' in email:
    spam=True
elif "buy now" in email:
    spam=True
elif 'subscribe' in email:
    spam=True
print("spam is", spam)

   
