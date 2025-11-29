#https://leetcode.com/problems/stable-subarrays-with-equal-boundary-and-interior-sum/

def stable_array(a):
    l=0
    r=len(a)-1
    sum=0
    ans=0
    sum2=0

    while(l<r):
        sum=a[l]+a[r]
        # print(sum)
        for j in range(l+1, r+1):
            sum2=sum2+a[j]
        if sum==sum2:
            ans+=1
        l+=1
        r-=1





    return ans

# a1=[9,3,3,3,9]

a1=[1,2,3,4,5]
ans=stable_array(a1)
print(ans)