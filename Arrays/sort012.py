
#sort 0,1,2

# set low := 0, mid := 0 and high := length of array – 1
# while mid <= high
# if arr[mid] = 0, then swap arr[mid] and arr[low], and increase low and mid by 1
# otherwise when arr[mid] = 2, swap arr[high] and arr[mid], decrease high by 1
# else increase mid by 1

def sort012(arr):
    low=0
    mid=0
    high=len(arr)-1

    while mid<=high:
        if arr[mid]==0:
            # swap mid and low elemnet
            arr[mid], arr[low]=arr[low], arr[mid]
            low+=1
            mid+=1

        elif arr[mid]==2:
            # swap mid and high
            arr[mid], arr[high]=arr[high], arr[mid]
            high-=1
        else:
            mid+=1


    return arr




arr = [2,0,2,1,1,0]
res = sort012(arr)
print(res)

