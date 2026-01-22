# 3sum

# anticlockwise
def krotated(arr, k):

    for i in range (k):
        temp=arr[0]
        for j in range(len(arr)-1):
            arr[j]=arr[j+1]

        arr[len(arr)-1]=temp

    return arr

# arr = [4,5,6,7,0,1,2]
# res = krotated(arr, 2) # rotate twice
# print(res)

# clockwise

def clockwise_rotate(arr, rotate):
    n=len(arr)
    for i in range(0, rotate):
        temp=arr[n-1]
        for j in range(len(arr)-1, 0, -1):
            arr[j]=arr[j-1]

        arr[0]=temp
    return arr

arr = [4,5,6,7,0,1,2]
res = clockwise_rotate(arr, 2) # rotate twice
print(res)