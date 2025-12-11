# https://leetcode.com/problems/non-decreasing-subsequences/description/.
# print subarrays when the order is incrasing
#[[[4, 6]], [[3, 7]], [[3, 7, 7]], [[7, 7]]]

def non_decreas_sub(a):
    l=[]
    for i in range(0, len(a)):
        for j in range(i+1, len(a)):
            temp=a[i:j+1]
            if(non_decreasing(temp)):
                l.append([temp])



    return l

def non_decreasing(t):
    flag=False
    for j in range(1,len(t)):
       if t[j-1]<=t[j]:
           flag=True
       else:
           flag=False
           break



    return flag

nums = [4,6,3,7,7]
res = non_decreas_sub(nums)
print(res)

