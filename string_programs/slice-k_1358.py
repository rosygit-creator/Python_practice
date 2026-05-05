
#  https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/


def countchar(input, k):
    t=[]

    for i in range (0, len(input)-k):
        for j in range(i, len(input)-k):
            temp=input[i:j+k]
            # check if any or atleast one  a, b, e is present in temp
            # if any(ch in temp for ch in 'abe'):
            # print(temp)
            # check if all a, b, e is present in temp
            if all(ch in temp for ch in 'abe'):
                t.append(temp)

    return t


ans=countchar("aaabeeeedfg", 3)
print(ans)

