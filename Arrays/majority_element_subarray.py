#https://leetcode.com/problems/minimum-distance-between-three-equal-elements-ii/description/

def majority(a):

    arr_len=0
    valid_subarray_count=0

    # k=-1
    # diff=0
    # min_value=float('inf')
    target=2
    for i in range(0,len(a)):
        count=0
        for j in range(i,len(a)):
            if a[j]==target:
                count+=1
            arr_len=j-i+1

        # count valid array length
            if count *2 > arr_len:
                valid_subarray_count+=1




    return valid_subarray_count

a1=[1,2,2,3]
# a1=[1,1,2,3,2,1,2]
ans=majority(a1)
print(ans)