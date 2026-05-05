# create a dict with name and age

data={}

while True:
    key = input("enter name  : ")
    if key == "":
        break
    value=input("enter age: ")
    if value=="":
        break
    data[key] = value
    
    
print("data: ", data)
