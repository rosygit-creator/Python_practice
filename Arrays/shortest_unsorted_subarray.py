#https://leetcode.com/problems/shortest-unsorted-continuous-subarray/description/

def shortest_unsorted_subarray(nums):
    l=[]
    temp=sorted(nums)
    left=0
    right=len(nums)-1

    while left<=right and nums[left]==temp[left]:
        left+=1

    while left <= right and nums[right] == temp[right]:
        right-=1

    length=right-left+1

    for i in range(left, right+1):
        l.append(nums[i])





    return l

a=[2, 6, 4, 8, 10, 9, 15]
ans=shortest_unsorted_subarray(a)
print(ans)