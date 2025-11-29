# https://leetcode.com/problems/increasing-triplet-subsequence/description/


def increasing_triplet_seq(a): # works when the input is consecutive

    for i in range(0, len(a)-2):
        if a[i]<a[i+1] and a[i+1]<a[i+2]:
            return True


    return

def increasing_triplet_non(nums):
    first = float('inf')
    second = float('inf')

    for num in nums:
        if num <= first:
            first = num
        elif num <= second:  # first < num <= second
            second = num
        else:
            return True  # first < second < num (third)

    return False




# a1=[1,2,3,4,5]
# a1=[5,4,3,5,6, 1,2 ]
# ans=increasing_triplet_seq(a1)
# print(ans)

a1=[2,1,5,0,4,6] # non consecutive
ans=increasing_triplet_non(a1)
print(ans)