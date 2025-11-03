# 3sum


def print_long_palin(input):
    sub=get_sub(input)
    longest=0
    print(f" sub is {sub}")
    for item in sub:

        fp=get_palin(item)
        print(f" fp is {fp} for item  {item}")
        print("---------------")
        if fp==True:
            longest=max(len(item),longest)
        # if len(fp)>longest:
        #     longest=res

    return longest





def get_palin(p):
    print(f"inside {p}")
    l1=[]
    s=0
    e=len(p)-1
    flag=True
    while(s<e):
        if p[s]!=p[e]:
            flag=False
            break
        s+=1
        e-=1

    # if flag==True:
    #     print(f" is palindrome {p}")
    return flag



def get_sub(s):
    l=[]
    for i in range(0,len(s)):
        for j in range(i+1,len(s)+1):
            # print(s[i:j]) # does ot take last value of j
            l.append(s[i:j])
    return l

ans=print_long_palin("babad")
print(ans)

