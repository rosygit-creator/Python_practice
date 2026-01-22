# https://leetcode.com/problems/replace-words/description/


def replace_words(input):
    dictionary = ["cat", "bat", "rat"]

    for d in dictionary:
        temp=input.split(" ")
        for i in range(0, len(temp)):
            for d in dictionary:
                index=temp[i].find(d)
                if index ==0:
                    temp[i]=d

    return ' '.join(temp)


ans=replace_words("the cattle was rattled by the battery")
print(ans)