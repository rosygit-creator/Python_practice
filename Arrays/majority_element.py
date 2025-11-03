
#Majority Element II - Elements occurring more than ⌊n/3⌋ times

def majority_element(arr):
    l=[]

    map={} # dictionary

    # Add current element to the dict
    for e in arr:
        map[e]=map.get(e,0)+1

    for key, value in map.items():
        if value > len(arr)//3: # floor value //
            l.append(key)

    return l



arr = [2, 2, 3, 1, 3, 2, 1, 1]
res = majority_element(arr)
print(res)

