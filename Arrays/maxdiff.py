

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

def maxdiff(arr):
 # arr.sort()
 res= 0
 ans=0
 flag=False
 l=[]

 for i in range(0,len(arr)-1):
     # res=0
     for j in range(i+1, len(arr)):
         diff=abs(arr[j]-arr[i])
         print(f"diff is {diff}")
         res=max(diff, res)
         print(f"res is {res}")






 return res

nums = [3,6,9,1] #1,3,6,9
ans=maxdiff(nums)
print(ans)