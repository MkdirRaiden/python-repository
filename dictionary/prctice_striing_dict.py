#mirror
alpha = 'abcdefghijklmnopqrstuvwxyz'
rev_alpha = alpha[::-1]
dic = dict(zip(alpha, rev_alpha))
my_string = input("Enter a word: ")
k = int(input('Enter the value of k: '))
string1=my_string[:k-1]
string2=my_string[k-1:]
for x in string2:
    string2 = string2.replace(x, dic[x])    
print(string1+string2) 
