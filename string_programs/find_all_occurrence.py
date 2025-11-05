# nput:  text =  "AABAACAADAABAABA", pattern = "AABA"
# Output: Pattern found at index 0, Pattern found at index 9, Pattern found at index 12

# note the overlap at pos12

def find_all_occurrence(input, part):
    count=0
    index = 0
    index = input.find(part, index)
    # print(f"index {index}")
    for i in range(0, len(input),len(part)):
        if index==-1:
            pass
        else:
            count += 1
        # print(f"index {index}")
        index=index+1
        index=input.find(part, index)
        # print(f"index2 {index}")
    return count

# Input: s1 = "AXY", s2 = "ADXCPY"
# Output: true
# Explanation: All characters of s1 are in s2 in the same order
#
# Input: s1 = "AXY", s2 = "YADXCP"
# Output: false
# Explanation: All characters are present, but order is not same.
#
# Input: s1 = "gksrek", s2 = "geeksforgeeks"
# Output: true

def longest_common(input, part):
    count=0
    index = 0
    for i in range(0,len(part)):
        index=input.find(part[i], index)
        if index > -1:
            count+=1
        else:
            pass
        # print(f"count {count} for {part[i]}")
        index=index+1
        # index = input.find(part[i],index)

    return count


# input=daabcbaabcbc, output =dab


def remove_all(input,part):
    start=0
    index=input.find(part)

    while index!= -1:
        input=input.replace(part, '')
        index = input.find(part)


    return input


#1
ans=find_all_occurrence("AABAACAADAABAABA","AABA")
print(ans)

#2 https://www.geeksforgeeks.org/dsa/given-two-strings-find-first-string-subsequence-second/
# ans=longest_common("abcde","ace")  #3 for ace
#
# print(ans)
#
# ans=longest_common("abc","def")  #0
# print(ans)

ans=longest_common("abcde","acbe")  #3 for ace, b is also in input but not in sequence
print(ans)

#3
ans=remove_all("daabcbaabcbc", "abc")
print(ans)

