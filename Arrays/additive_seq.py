# https://leetcode.com/problems/additive-number/description/

def additive_sequence(input):
    d={}
    for item in input:
        if item not in d:
            d[item]=1
        else:
            d[item] += 1

    # order dictionary by values

    sorted_d = sorted(d.items(), key=lambda x: x[1]) # ascending order by value

    sorted_d = sorted(d.items(), key=lambda x: x[1], reverse=True) # descending order by value

    return sorted_d

a=[1,2,2,2,2,3,4,4,5,5,5]
ans=additive_sequence(a)
print(ans)
