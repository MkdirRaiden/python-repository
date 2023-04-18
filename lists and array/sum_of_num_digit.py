lst=[33, 1, 345, 111, 0]
def digits_sum(lst):
    sum_digits=[]
    for i in lst:
        digit=[]
        while i%10:
            d=i%10
            digit.append(d)
            i//=10
            if i==0:
                break
        sum_digits.append(sum(digit)) 
    return sum_digits 
print(f"The sum of the digits of the elements of the list: {lst} are: {digits_sum(lst)}")          
#other method
s=[]
for i in lst:
    dig=[]
    for j in str(i):
        dig.append(int(j))
    s.append(sum(dig))
print(f"the sum of digits of the element in list: {lst} are: {s}") 
         