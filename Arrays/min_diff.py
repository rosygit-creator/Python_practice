#https://leetcode.com/problems/minimum-distance-between-three-equal-elements-ii/description/

def min_diff(a):
    count=1
    k=-1
    diff=0
    min_value=float('inf')

    for i in range(0,len(a)):
        count=1
        for j in range(i+1,len(a)):
            if a[i]==a[j] and count < 3:
                k=j
                count+=1
            if a[i]==a[j] and count==3:
                diff=abs(i-j)+abs(j-k)+abs(i-k)
                min_value=min(min_value,diff)

    return min_value

a1=[1,2,1,1,3]
# a1=[1,1,2,3,2,1,2]
ans=min_diff(a1)
print(ans)