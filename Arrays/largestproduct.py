

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

def longestConsecutive(arr):
 res= float('-inf')
 ltr=1
 rtl=1
 n=len(arr)
 for i in range(n):
  if ltr==0:
   ltr=1
  if rtl==0:
   rtl=1
  ltr*=arr[i]

  j=n-i-1
  rtl*=arr[j]

  res=max(res, rtl,ltr)

 return res

nums = [-2, 6, -3, -10, 0, 2]
ans=longestConsecutive(nums)
print(ans)