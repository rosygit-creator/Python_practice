# Sorted subsequence of size 3 - a[i] < a[j] < a[k] and i < j < k in 0(n) time.
# Input: arr[] = {12, 11, 10, 5, 6, 2, 30}
# Output: 5, 6, 30
# Explanation: As 5 < 6 < 30, and they
# appear in the same sequence in the array
#
# Input: arr[] = {1, 2, 3, 4}
# Output: 1, 2, 3 OR 1, 2, 4 OR 2, 3, 4
# Explanation: As the array is sorted, for every i, j, k,
# where i < j < k, arr[i] < arr[j] < arr[k]
#
# Input: arr[] = {4, 3, 2, 1}
# Output: No such triplet exists.

def sorted_subsequence(a):
    l=[]
    for i in range(1, len(arr)-1):
        print(f"{i}")
        print(f"{a[i-1]},{a[i]}, {a[i+1]}")
        if a[i]>a[i-1] and a[i]<a[i+1]:
            l.append([a[i-1], a[i], a[i+1]])
            # break


    return l




arr = [12, 11, 10, 5, 6, 2, 30]
res = sorted_subsequence(arr)
print(res)

