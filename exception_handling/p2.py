
def func1(age1):
    if age1 <0:
        raise ValueError("age is less than 0")

    return age1
  
try:
    age=int(input("enter age1 : "))
    func1(age)
except ValueError as e:
    print(e)
# import math


# try:
#     age2=int(input("enter age2 : "))
#     y=math.sqrt(age2)
# except ValueError:
#     print("age cannot be negative")
