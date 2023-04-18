#to check if a given string is a python keyword
import keyword
keys=['for', 'hello', 'if', 'string', 'while', 'raiden', 'tuple', 'hey']
for i in range(len(keys)):
    if keyword.iskeyword(keys[i]):
        print(keys[i]+' '+'is a python keyword')
    else:
        print(keys[i]+' '+'is not a python keyword')
import keyword
print(f'The list of keywords are: {keyword.kwlist}')
