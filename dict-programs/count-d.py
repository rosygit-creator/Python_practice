# create a dict with name and age

data={"A":0,"B":1,"C":0}

while True:
    key = input("enter name A/B/C : ")
    if key == "":
        break
    
    data[key] += 1
    
    
print("data: ", data)
