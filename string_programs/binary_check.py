#https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/

def croack1(s):
    v=["01","00","10","11"]
    # max_len=0
    # temp=""

    if all(v1 in s for v1 in v):
        return True
    else:
        return False

ans=croack1("00110110")
print(ans)