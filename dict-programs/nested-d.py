# create a dict with name and age
# https://python-course.eu/python-tutorial/working-with-dictionaries-and-while-loops.php
modes={}

while True:
    
    mode = input("enter mode cook/grill/pop  : ")
    if mode == "":
        break
    duration = input("enter duration: ")
    
    if duration=="":
        break
    type = input("add type : ")
    if type=="":
        break


    modes[mode]={
        "duration":duration,
        "type":type
    }
   

print("data: ", modes)
