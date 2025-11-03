

# def longestConsecutive(arr):
#   prod=1
#   res=0
#   for i in range(0,len(arr)):
#    prod=arr[i]
#    for j in range(i+1,len(arr)):
#     prod=prod*arr[j]
#     print(f"prod is {prod}")
#     if prod>res:
#       res=prod
#
#   return res

# O(n)

def peakelement(arr):
 res= float('-inf')
 flag=False
 l=[]

 for i in range(1,len(arr)-1):
   if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
     flag =True
     l.append(arr[i])
   else:
     flag=False



 return l

nums = [1, 5, 4, 5, 7, 8, 3]
ans=peakelement(nums)
print(ans)