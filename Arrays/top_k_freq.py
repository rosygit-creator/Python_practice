# Input: arr[] = [3, 1, 4, 4, 5, 2, 6, 1], k = 2
# Output: [4, 1]
# Explanation: Frequency of 4 is 2 and frequency of 1 is 2, these two have the maximum frequency.
#
# Input: arr[] = [7, 10, 11, 5, 2, 5, 5, 7, 11, 8, 9], k = 4
# Output: [5, 11, 7, 10]
# Explanation: Frequency of 5 is 3, frequency of 11 is 2, frequency of 7 is 2, and frequency of rest is 1  but 10 is largest .
import heapq

def top_k_frequency(arr, k):
    pq = []

    output=[0] * len(pq)
    map={}
    # dict will store list elements with freq
    for e in arr:
        map[e]=map.get(e,0)+1

    # priority q to kepe track of values


    for key, value in map.items():
        heapq.heappush(pq, [value,key]) #  storing in value, key so that most frequency elemnets are stored

        #if heap size >k pop
        if len(pq) > k:
            heapq.heappop(pq)

    while pq:
        output=heapq.heappop(pq)[1]
        # for val in output:
        # print(f"{output}")
        # print(f"{output[0]}")
        break




    return output

# arr = [10, 20, 30, 60, 30, 60, 10] for this input best solution is hashmap/dict
arr=[40, 40,70, 90, 30, 50, 60, 10]
res = top_k_frequency(arr, 2)
print(res)

