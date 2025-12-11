# Example 2:
#
# Input: words1 = ["amazlcon","apple","facebook","google","leetcode"], words2 = ["lc","eo"]
#
# Output: ["leetcode"]

def word1(words1, words2):
    result=[]
    for item in words1:
        for w in words2:
            if all(c in item for c in w):
                print("inside")
                result.append(item)
                print(f" w is {w}  true {result}")  #
    return

words1 = ["amalczon", "apple", "facebook", "google", "leetcode"]
words2 = ["lcd"]
# ans=word1(words1, words2)
# print(ans)


# find words1 which contain either words2
def word_subsets(words1, words2):
    result=[]
    count=0
    for item in words1:
        for w in words2:
            if all(c in item for c in w):
                # count+=1
                if item not in result:
                    result.append(item)
            # print(f" w is {w}  true {result}") #
    return result



words1 = ["amalczon","apple","facebook","google", "leetcode"]
words2 = ["lc", "eo"]
ans=word_subsets(words1, words2)
print(ans)

# check if both of words2 are in words1

def word_subsets_all(words1, words2):
    result=[]
    count=0
    flag=False
    for item in words1:
        for w in words2:
            if all(c in item for c in w):
                flag=True
            else:
                flag=False
                break
        if flag==True:

            count+=1
            result.append(item)
            # print(f"true {count}") #

    return result

words1 = ["amalczon","apple","facebook","google", "leetcode"]
words2 = ["lc", "ee"]
# ans=word_subsets_all(words1, words2)
# print(ans)