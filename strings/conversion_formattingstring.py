def print_formatted(number):
    for i in range(1, number+1):
        d = str(i)
        o = format(i, 'o')
        h = format(i, 'X')
        b = format(i, 'b') 
        l = len(format(number, 'b'))
        print(d.rjust(l), o.rjust(l), h.rjust(l), b.rjust(l))
        print('\r')
while True:        
    try:        
        n = int(input())        
        print_formatted(n)
    except EOFError:
        break
          