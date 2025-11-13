
# Example:
# Input: n = 7, arr[] = [1, 2, 3, 6, 3, 6, 1]
# Output: 1, 3, 6
# Explanation: The numbers 1 , 3 and 6 appears more than once in the array.
#
# Input : n = 5, arr[] = [1, 2, 3, 4 ,3]
# Output: 3
# Explanation: The number 3 appears more than once in the array.

def find_duplicate_aux_array(arr):
    n=len(arr)
    freq=[0] * n  # [0, 0, 0, 0, 0, 0, 0] freq can only have index 1-6
    # print(f"freq {freq}")
    output=[]

    for e in arr:
        freq[e]+=1 # list stores the frequencues and not the arr value freq [0, 2, 1, 2, 0, 0, 2]
        print(f"freq {freq}")

    for i in range(n):
        if freq[i] > 1 :
            # print(freq[e])
            output.append(i) # [1, 3, 6, 3, 6, 1]



    return output

# arr = [10, 20, 30, 60, 30, 60, 10] for this input best solution is hashmap/dict
arr=[1, 2, 3, 6, 3, 6, 1]

res = find_duplicate_aux_array(arr)
print(res)

