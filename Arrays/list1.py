list1=[1,2,3,4]
list2=['apple','banana','orange']
list3=["a","b","abc"]

#prints 2,3,4
print(list1[1:4]) # slicing

#prints all elems
print(list1)

#append a list
list2.append('cherry')

print(list2[0:4])

#delete elem
del list3[1]

print(list3[0:2])

t3=(1,2,3,4)
list1=[1,2,3,4]
list2=[4,5,6,1,3]
list3=[]

#check 3 is present in tuple

for i in list1:
 if i not in list3:
  list3.append(i)

for j in list2:
 if j not in list3:
  list3.append(j)

print(list3)