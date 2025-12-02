# https://leetcode.com/problems/product-of-array-except-self/description/


def product_self(a):
    result=[1] * len(a)
    k=0

    for i in range(1, len(a)):
        if k!=i:
            result[k]=result[k]*a[i]


    return





# a1=[1,2,3,4,5]
# a1=[5,4,3,5,6, 1,2 ]
# ans=increasing_triplet_seq(a1)
# print(ans)

a1=[2,1,5,0,4,6] # non consecutive
ans=product_self(a1)
print(ans)