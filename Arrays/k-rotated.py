# 3sum


def krotated(arr, k):

    # minDiff = float('inf')
    target=0

    # Generating all triplets
    for i in range (k):
        temp=arr[0]
        for j in range(len(arr)-1):
            arr[j]=arr[j+1]

        arr[len(arr)-1]=temp

    for item in arr:
        if item==target:
            print(arr.index(item))




    return arr

arr = [4,5,6,7,0,1,2]
res = krotated(arr, 2)
print(res)

