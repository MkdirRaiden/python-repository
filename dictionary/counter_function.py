from collections import Counter
X = int(input())
val = list(map(int, input().split()))
dic = Counter(val)
N = int(input())
tem = []
for i in range(N):
    size, price = input().split()
    if int(size) in list(dic.keys()) and dic[int(size)]>=1:
        tem.append(int(price))
        dic[int(size)]-=1
    else:
        continue
print(sum(tem))        