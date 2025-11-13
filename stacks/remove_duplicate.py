# given s="azzxzy", result="axzy"

def stack1(s1):
    output=[] # list ot stack
    i=0
    while i<len(s1):
        # len(output)==0 is required
        if len(output)==0 or s1[i]!=output[-1]: # string char is not equal to stack top/last element
            output.append(s1[i])
        else:
            output.pop()
        i+=1


    return output



a="azzxzy"
ans=stack1(a)
print(ans)