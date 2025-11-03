# 3sum

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k,
# and j != k, and nums[i] + nums[j] + nums[k] == 0.

def findTriplets(arr):
    res = []
    sum=0
    arr.sort()
    n = len(arr)



    # Generating all triplets
    for i in range(n - 2):
        left, right = i + 1, n - 1
        while left<right:
            sum=arr[i]+arr[left]+arr[right]
            if sum == 0:
                res.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1
            elif sum < 0:
                left+=1
            else:
                right-=1




    return res

arr = [0, -1, 2, -3, 1]
res = findTriplets(arr)
# print(res)

for triplet in res:
    print(triplet)