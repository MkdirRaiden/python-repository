l1=["Safiul", "Sonali","Ritu","Rajneesh"]
for item in l1:
    if item[0]=="s".upper():#or item.startswith("s").upper()
        print(f"Good morning! {item}")
    else:
        break 
