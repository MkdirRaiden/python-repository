my_string= "welcome to programming at our website"
words= my_string.split()   #gives a list of words
rev_string=' '.join(reversed(words)) #or we can also use (.join(words[::-1]))
print(rev_string)
#using list comprehension method
text="Welcome to Norway. It is a fine place to visit."
my_list=[words for words in text.split() if "o" or "i" in words]
print(" ".join(reversed(my_list)))