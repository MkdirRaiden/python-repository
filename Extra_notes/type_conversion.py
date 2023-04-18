s = '6' #string
n = int(s, 10) #base 10
print(n)
s1 = '0100'
n1 = int(s1, 2) #base 2
print(n1)
f = float(n1)
print(f)
print(ord('4')) #ord() converts a character into a integer
print(ord('z'))
print(hex(3), oct(45)) #converts integer to string
# conversion to dictionary is only possible if the elements are in pairs 
val = [{1, 3}, [5, 0], ['hi', 3], ['s', 10]]
print(dict(val))