# https://www.hackerrank.com/challenges/alternating-characters/problem?isFullScreen=true

def is_alternate_Letter(s):
    i=0
    output=""
    while i<len(s):
        if i <len(s)-1 and s[i]==s[i+1]:
            output=output+s[i]
            output=output+""
            i+=2
        else:
            output=output+s[i]
            i+=1

        # output="".join(s)
    return "".join(output)

s="AAABBAABBA"

ans=is_alternate_Letter(s)
print(ans)