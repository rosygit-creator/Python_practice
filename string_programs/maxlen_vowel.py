#https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/

def croack1(s):
    v="aeiou"
    max_len=0
    temp=""

    for i in range(0, len(s)):
        if s[i] in v:
            temp=temp+s[i]
        else:
            if len(temp)>max_len:
            # max_len=max(max_len, len(temp))
                max_len=len(temp)
                result=temp
                temp=""
    
    return result



ans=croack1("abciiidef")
print(ans)