#  https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/description/

# Input: s = "bab", t = "aba"
# Output: 1
# Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.

from  collections import Counter

def reverse_string(s, t):
    ct=Counter(s)
    temp=[]
    result=""

    for ch in t:
        ct[ch]-=1
        if ct[ch]<0:
            result=result+ch
        
    

    return result

def reverse_string1(s,t):
    result1=""
    map={}
         
    for c in s:
        map[c]=map.get(c, 0)+1

    for ch in t:
        for k, v in map.items():
            print("ch is", ch)
            if ch==k:
                map[k]-=1
                print("v is", v)
                print(map)
                if map[k]<0:
                    result1=result1+k
                break
            
    
    return result1


s = "bab"
t="aba"
# ans=reverse_string(s, t)

ans1=reverse_string1(s,t)

print("ans", ans1)