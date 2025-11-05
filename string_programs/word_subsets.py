# Example 2:
#
# Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["lc","eo"]
#
# Output: ["leetcode"]


def word_subsets(words1, words2):
    result=[]
    count=0
    for item in words1:
        for w in words2:
            if all(c in item for c in w):
                count+=1
                result.append(item)
            # print(f"true {count}") #

    return result

words1 = ["amazon","apple","facebook","google", "leetcode"]
words2 = ["lc"]
ans=word_subsets(words1, words2)
print(ans)