def greater(a, b, c):
    if a>b:
        greater=a
    else:
        greater=b
    if c>greater:
        greater=c 
    return greater
print(greater(34,56,100))                  
