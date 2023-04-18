import re
string = input()
sub_string = input()
pattern = re.compile(sub_string)
m = pattern.search(string)
if not m:
    print('(-1, -1)')
else:
    while m:
        print(f"({m.start()}, {m.end()-1})")
        m = pattern.search(string, m.start()+1)    
