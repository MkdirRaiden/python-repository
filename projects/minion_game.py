def minion_game(string):
    all_substrings = [string[i:j] for i in range(len(string)) for j in range(i+1, len(string)+1)]
    v_substrings = [x for x in list(filter(lambda x: x[0] in 'AEIOU', all_substrings))]
    c_substrings = [x for x in all_substrings if x not in v_substrings]
    k_strings = list(set(v_substrings))
    s_strings = list(set(c_substrings))
    score_k = []
    score_s = []
    for j in k_strings:
        count = 0
        for i in range(len(string)):
            if string.startswith(j, i):
                count+=1
        score_k.append(count)
    for j in s_strings:
        count = 0
        for i in range(len(string)):
            if string.startswith(j, i):
                count+=1
        score_s.append(count)        
    if sum(score_k) == sum(score_s):
        print('Draw')    
    elif sum(score_k)>sum(score_s):
        print(f"Kevin {sum(score_k)}")
    else:
        print(f"Stuart {sum(score_s)}")
minion_game("BANANA") 
#Alternative 
def minion_game(string):
    v, c = 0, 0
    for i in len(string):
        if string[i] in 'AEIOU':
            v = v+len(string)-i
        else:
            c = c+len(string)-i            
    if v == c:
        print('Draw')
    elif v<c:
        print(f"Stuart {c}")
    else:
        print(f"Kevin {v}")    
n = input('Enter a string: ')
minion_game(n)             