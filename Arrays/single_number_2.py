
# find elemnet that appears only once in an array

def single_number_2(a):
    a.sort()
    for i in range (1, len(a),3):
        if a[i-1]!=a[i]:
            return a[i-1]
        else:
            pass


# a=[5,5,5,2,4,4,4]
# ans=single_number_2(a)
# print(ans)

a=[2,2,1,2,1,1,4,3,4,4]
ans=single_number_2(a)
print(ans)