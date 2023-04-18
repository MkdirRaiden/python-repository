thousands = 'M{0,3}'
hundreds = '(CM|CD|D?C{0,3})'
tens = '(XC|XL|L?X{0,3})'
units = '(IX|IV|V?I{0,3})'
regex_pattern = r"%s%s%s%s$"%(thousands, hundreds, tens, units)	
import re
print(str(bool(re.match(regex_pattern, input()))))
import re
n = int(input())
for i in range(n):
    name, email = input.split(' ')
    pattern = r"<[a-z][a-zA-Z0-9\-\.\_]+@[a-zA-Z]+\.[a-zA-Z]{1,3}>"
    if bool(re.match(pattern, email)):
        print(name, email)    
    