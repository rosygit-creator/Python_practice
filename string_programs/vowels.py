#Vowels of All Substrings# 3sum
#
# Input: word = "aba"
# Output: 6
# Explanation:
# All possible substrings are: "a", "ab", "aba", "b", "ba", and "a".
# - "b" has 0 vowels in it
# - "a", "ab", "ba", and "a" have 1 vowel each
# - "aba" has 2 vowels in it
# Hence, the total sum of vowels = 0 + 1 + 1 + 1 + 1 + 2 = 6.

def count_vowel(input):
    sub_string=[]
    sum=0

    for i in range(0, len(input)):
        for j in range(i+1, len(input)+1):
            print(input[i:j])
    # print(sub_string)

            count_v=is_Vowel(input[i:j])

            # print(count_v)
            sum = sum + count_v

    return sum

def is_Vowel(s1):
    count=0
    vowel="aeiouAEIOU"

    for c in s1:
        if vowel.find(c) > -1: # increase count for each vowel letter in s1
            count+=1

    return count

ans=count_vowel("aBa")
print(ans)

