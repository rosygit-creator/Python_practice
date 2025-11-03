# 3sum closest
# Given an integer array nums of length n and an integer target, find three integers in
# nums such that the sum is closest to target.
#
# Return the sum of the three integers.


def findTriplets(arr):
    res = []
    sum=0
    arr.sort()
    n = len(arr)
    diff=0
    target=4
    res=0
    minDiff = float('inf')


    # Generating all triplets
    for i in range(n - 2):
        left, right = i + 1, n - 1
        while left<right:
            sum=arr[i]+arr[left]+arr[right]
            diff=abs(sum-target)

        # if diff is < mindiff then sum is closer to target

            if diff<minDiff:
                minDiff=diff
                res=sum
            elif diff==minDiff:
                res=max(res, sum)

            if sum < target :
                left+=1
            else:
                right-=1

    print(f"res is %% {res}")


    return res

arr = [-1, 2, 2, 4]
res = findTriplets(arr)
print(res)

