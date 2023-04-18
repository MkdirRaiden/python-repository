class reverse:
    def __init__(self, data):
        self.data=data
        self.index=len(data)
    def __iter__(self):
        return self
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        else:
            self.index-=1    
            return self.data[self.index]
data1 = reverse([1, 3, 1, 6, 3, 7])
for item in data1:
    print(item, end=' ') 
print('\r')                        
#Another method of creating iterators is generators
def Reverse(data):
    for i in range(len(data)-1, 0-1, -1):
        yield data[i]
rev = Reverse('Muktadir')
for chr in rev:
    print(chr)                