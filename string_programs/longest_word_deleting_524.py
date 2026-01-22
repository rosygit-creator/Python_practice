# https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/description/


def longest_word_deleting(s1, dict1):

    dict1.sort(key=len)
    l=[]
    max=0
    for item in dict1[::-1]:
        if all(c in s1 for c in item):
            if len(item) > max:
                l.clear()
                l.append([item])
                max=len(item)



    return l


dictionary = ["ale","apple","monkey","plea"]
s="abpcplea"

ans=longest_word_deleting(s, dictionary)
print(ans)

