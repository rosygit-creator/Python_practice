# create a dict with name and age

list_of_dict=[]


while True:
    
    name = input("enter name  : ")
    if name == "":
        break
    # data['name']=name
    age=int(input("enter age: "))
    if age=="":
        break

    list_of_dict.append({
        "name":name,
        "age":age
    })
   
    
print("data: ", list_of_dict)
