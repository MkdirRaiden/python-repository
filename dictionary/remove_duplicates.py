string = input("Enter a string: ")
k = int(input("Enter value of k: "))
l = len(string)
start = 0
res = []
for i in range(k):
    res.append(string[start:start+k])
    start = start + k
for items in res:
    print(''.join(dict.fromkeys(items)))
#alternative
s = ''
count = 0
for i in string:
    if i not in s:
        s+=i
    count+=1
    if count==k:
        print(s)
        s=''
        count=0  