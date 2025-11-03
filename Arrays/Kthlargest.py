# Example 1:
#
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5

import heapq  # priory queue

def Kthlargest(arr,k):
    pq=[]
    print(k)

    # Add current element to the min heap
    for e in arr:
        heapq.heappush(pq,e)
    # print(pq)
        # If heap exceeds size K, remove smallest element
        if len(pq) > k:
            heapq.heappop(pq)

    # Top of the heap is the K'th largest element

    return pq[0]



arr = [12, 3, 5, 7, 19]
res = Kthlargest(arr, 3)
print(res)

