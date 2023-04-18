txt="   i want to be a programmar, a good coder just for fun."
print(txt.strip())
print(txt.upper())
print(txt.capitalize())
print(txt.count("o"))
print(txt.endswith("fun."))
print(txt.replace("fun", "knowledge"))
print(txt.index("to"))
print(txt.partition(","))
if 'coder' in txt:
    print("yes, it is present.")
print(txt.casefold())   
print(txt.split(",")) 
print(txt.find("g"))
txt="I'm Muktadir Ahmed, and I'm {} years old. I've been living here for {} years."
age=26
years=4
print(f"I'm Muktadir Ahmed aged {age} years old and I've been working here for {years} years.")
txt="  i'm muktadir ahmed."
txt=txt.strip()
for x in txt:
    print(x)
txt1="hey! how are you."    
txt1=txt1.capitalize()
i=0
while i<len(txt1):
    print(txt1[i])
    i+=1
