# https://leetcode.com/problems/find-all-anagrams-in-a-string/

def find_all_anagram(input,part):

    l1 = []
    temp=""

    len_p=len(part) # 3
    for i in range(0,len(input)-len(part)+1):
        temp=input[i:i+len_p]
        # check  all char of part are in temp then temp is an anagram
        if all(c in temp for c in part):
            # print(f" {temp} is yes")
            l1.append(i)


    return l1


s= "cbaebabacb"  # 11
p = "abc"

ans=find_all_anagram(s,p) #ans is 0, 6, 7

print(ans)


s = "abab"
p = "ab"

ans=find_all_anagram(s,p)

print(ans) # [0,1,2]
