# 3sum

# Find First and Last Position of Element in Sorted Array


def first_last(arr):

    # minDiff = float('inf')
    first=-1
    last=-1
    target=8
    res=[]

    # Generating all triplets

    for j in range(len(arr)):
        if arr[j]==target:
            if first==-1:
                res.append(j)
            elif last==-1:
                res.append(j)

    print(f" first {first} and last is {last}")

    return res




arr = [5,7,7,8,8,10]
res=first_last(arr)

print(res)
