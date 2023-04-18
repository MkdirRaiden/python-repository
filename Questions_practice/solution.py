from json.encoder import INFINITY
block = [
    {
        'gym':False,
        'school':True,
        'store':False
    },
    {   'gym':True,
        'school':False,
        'store':False
    },
    {   'gym':True,
        'school':True,
        'store':False
    },
    {
        'gym':False,
        'school':True,
        'store':False
    },
    {
        'gym':False,
        'school':True,
        'store':True
    }
]
reqs = ['gym', 'school', 'store']
D = []
i = 0
while i<len(block):
    d = []
    for j in range(3):
        count = 0
        rev_count = 0
        if i == 0:
            for dic in block:
                if dic[reqs[j]]==True:
                    d.append(count)
                    break   
                count+=1
        elif i == len(block)-1:
            for dic in reversed(block):
                if dic[reqs[j]]==True:
                    d.append(rev_count)
                    break 
                rev_count+=1
        else:
            for dic in block[i:len(block)]:
                if dic[reqs[j]]==True:
                    break
                else:
                    if dic is block[-1]:
                        count=INFINITY
                    else:    
                        count+=1
            for dic in reversed(block[0:i+1]):
                if dic[reqs[j]]==True:
                    break
                else:
                    if dic is block[0]:
                        rev_count=INFINITY
                    else:      
                        rev_count+=1
            if count==INFINITY:
                d.append(rev_count)
            elif rev_count==INFINITY:
                d.append(count)
            else:                    
                d.append(min(count, rev_count)) 
    D.append(sum(d)) 
    i+=1  
print(D)            
print(f"The required block is at {D.index(min(D))+1} position.")                                
        