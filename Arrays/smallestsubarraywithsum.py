# Input: x = 51, arr[] = [1, 4, 45, 6, 0, 19]
# Output: 3
# Explanation: Minimum length subarray is [4, 45, 6]
#
# Input: x = 100, arr[] = [1, 10, 5, 2, 7]
# Output: 0
# Explanation: No subarray exist

def smallestsubarraywithsum(arr):
    n=len(arr)
    res = float('inf')
    target=58
    count=0

    for i in range(n):
        sum=arr[i]

        for j in range(i+1,n):
            sum=sum+arr[j]
            # count+=1

            if sum > target:
                # res=min(res, count) # use count or as below
                res=min(res, j-i+1)
                break

    return res

# arr = [10, 20, 30, 60, 30, 60, 10] for this input best solution is hashmap/dict
arr=[1, 4, 45, 6, 10, 19]
res = smallestsubarraywithsum(arr)
print(res)

