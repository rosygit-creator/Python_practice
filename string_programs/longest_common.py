# Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.
#
# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
#
# For example, "ace" is a subsequence of "abcde".

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


# ans=longest_common("abcde","ace")  #3 for ace
#
# print(ans)
#
# ans=longest_common("abc","def")  #0
# print(ans)

ans=longest_common("abcde","acbe")  #3 for ace, b is also in input but not in sequence
print(ans)
