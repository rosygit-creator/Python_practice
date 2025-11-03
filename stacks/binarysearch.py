def binarysearch(a):
    target=12
    low=0
    high=len(a)-1

    while low<=high:
        mid=(low+high)//2   # floor division
        if a[mid]==target:
            return mid
        elif a[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1



sorted_list = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
index=binarysearch(sorted_list)
print(index)
