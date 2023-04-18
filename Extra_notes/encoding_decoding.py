a = 'Muktadir' 
b = b'Muktadir' #byte object
c = a.encode('ASCII') #by default UTF-8 technique is used
if b==c:
    print('encode successful')
else:
    print('encode unsuccesful') 
c = b.decode('ASCII')
if c==a:
    print('decode successful')
else:
    print('decode unsuccesful')           