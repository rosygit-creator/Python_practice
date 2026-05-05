# https://www.geeksforgeeks.org/dsa/rearrange-array-such-that-even-positioned-are-greater-than-odd/
def even_odd(a):
    # this works
    for i in range(0, len(a)-1,2):
        if i%2==0 and a[i]<a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]

    # for i in range(0,len(a)-1):
    #     if (i+1)%2==0 and a[i]<a[i+1]:
    #         a[i], a[i + 1] = a[i + 1], a[i]
    return a

arr = [ 1, 3, 2]
ans=even_odd(arr)
print(ans)