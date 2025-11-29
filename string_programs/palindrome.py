# 3sum


def palindrome(input):
    s=0
    e=len(input)-1
    flag=True
    while(s<e):
        if input[s]!=input[e]:
            flag=False
            break
        s+=1
        e-=1

    return flag







arr = "ma"
res = palindrome(arr)
print(res)

