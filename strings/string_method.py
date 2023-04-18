mystring="hey! how are You boy?"\
"Are you free tonight? let's have some real fun. "\
"will you?"
print(mystring)
print(mystring[::-1])
mylist=mystring.split(' ')
revstring=' '.join(reversed(mylist))
print(revstring)
newlist=[x for x in mylist if "o" not in x]
print(newlist)
