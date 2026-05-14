# https://www.hackerrank.com/challenges/funny-string/problem?isFullScreen=true

def is_strong_password(p):
    l1=[]
    l2=[]
    rev=""

    for c in p:
        l1.append(int(ord(c)))
    
    rev=p[::-1]

    for c in rev:
        l2.append(int(ord(c)))

    for i in range(0, len(l1)-1):
        if abs(l1[i]-l1[i+1])!=1 or abs(l2[i]-l2[i+1])!=1:
            return False
    # print(rev)
    return  True

s="lmnoq"
ans=is_strong_password(s)
print(ans)