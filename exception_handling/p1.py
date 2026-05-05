# try:
#     age=int(input("enter age1 : "))
# except ValueError:
#     print("value is not an integer")
import math


try:
    age2=int(input("enter age2 : "))
    y=math.sqrt(age2)
except ValueError:
    print("age cannot be negative")
