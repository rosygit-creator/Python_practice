def longestConsecutive(arr):
 if not arr:
  return 0
 # Sort the array
 arr.sort()

 res = 1
 cnt = 1

 # Find the maximum length by traversing the array
 for i in range(1, len(arr)):

  # Skip duplicates
  if arr[i] == arr[i - 1]:
   continue

  # Check if the current element is equal
  # to previous element + 1
  if arr[i] == arr[i - 1] + 1:
   cnt += 1
  # else:
  #  # Reset the count
  #  cnt = 1
 # Update the result
   res = max(res, cnt)

 return res

if __name__ == "__main__":
    arr = [2, 2,3,1,4,5,6 ]
    print(longestConsecutive(arr))