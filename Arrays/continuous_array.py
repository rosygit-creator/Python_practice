
#  https://leetcode.com/problems/contiguous-array/description/
#  brute force
def continuous_array(a):
    l=[]
    maxlen=0

    for i in range(0, len(a)):

        for j in range(i+1,len(a)):
            temp=a[i:j+1]
            # print(temp)
            if temp.count(0)==temp.count(1):
                # l=j-i+1
                l.append([temp])
                # maxlen=max(maxlen, len(l)) to find maxlength of such array
                # print("l is", l)
            # print(temp)






    return maxlen

nums = [1, 0, 0, 1, 0, 1, 1]
ans=continuous_array(nums)
print("ans is ", ans)
print(len(ans))




