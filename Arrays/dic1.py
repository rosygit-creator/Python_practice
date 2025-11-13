# d1={'Name': 'Zara', 'Age': 7, 'Class': 'First'}
#
# print d1['Name']
# del d1['Name']
#
# print d1
#
# print str(d1)
# print d1.keys()
# print d1.values()


# find all subarrays

# def sub_array(arr):
#     an=[]
#     for i in range(0,len(arr)):
#         for j in range(i,len(arr)):
#
#             res=arr[i:j+1]
#             if res not in an:
#                 an.append(res)
#             # print(res)
#     return an
#
# a=[1,2,2]
# ans=sub_array(a)
# print(ans)


def test_s(s):
    print("inside")
    l1=[]
    for c in s:
        l1.append([c,s.count(c)])
    # print(l)
    return l1

l=test_s("hhello")
print(l)