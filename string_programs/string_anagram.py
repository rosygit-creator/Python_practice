# Input: strs = ["eat","tea","tan","ate","nat","bat"]
#
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

def string_anagram(input):

    # if len(input)==0:
    #     return 0
    l1 = []

    for i in range(0,len(input)-1):
        for j in range(i+1,len(input)):

            if sorted(input[i])==sorted(input[j]):
                l1.append([input[i],input[j]])
                # print(sorted(input[i]))

    return l1





s=["eat","tea", "tan","ate","nat","bat"]

ans=string_anagram(s)

print(ans)

