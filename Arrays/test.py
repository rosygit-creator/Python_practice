def findUnique(arr):
    res = 0

    # Find XOR of all elements
    for num in arr:
        res ^= num
        print("res ", res)

    return res


if __name__ == '__main__':
    arr = [2, 3, 5, 4, 5, 3, 4]
    print(findUnique(arr))