
import json
def compare_files():
 with open("f6.txt",'r') as f:
  data1=json.load(f)

 with open("f7.txt",'r') as f1:
  data2=json.load(f1)

 return data1==data2


result=compare_files()
assert result==True


# p2=json.loads(f3)
#
# print(p1)
# print(p2)

