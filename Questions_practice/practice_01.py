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
for dic in block:
    i = block.index(dic)
    d = []
    for j in range(3):
        if dic[reqs[j]]==True:
            d.append(0)
        else:
            count=0
            rev_count=0
            if i==0:
                for dic in block[i+1:]:
                    count+=1
                    if dic[reqs[j]]==True:
                        break  
                d.append(count)
            elif i==len(block)-1:
                for dic in reversed(block[0:i]):
                    print(dic)
                    rev_count+=1
                    if dic[reqs[j]]==True:
                        break
                d.append(rev_count)    
            else:
                for dic in block[i+1:]:
                    count+=1
                    if dic[reqs[j]]==True:
                        break 
                for dic in reversed(block[0:i]):
                    rev_count+=1
                    if dic[reqs[j]]==True:
                        break               
                d.append(min(count, rev_count))
    print(d)        
    D.append(sum(d))
print(D)  
print(f"The required block is at {D.index(min(D))+1}th position.")                      