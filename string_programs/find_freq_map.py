#https://www.hackerrank.com/challenges/migratory-birds/problem?isFullScreen=true

def croack1(s):
    map={}
    max_v=0
    result=0
    temp=0

    for c in s:
        map[c]=map.get(c, 0)+1
    
    max_v=max(map.values()) # prints 5 in [1,1,2,3,2, 2, 3, 3,3,3,4]
    # max_v=max(map.keys()) # prints 4, in [1,1,2,3,2, 2, 3, 3,4]
    print("max_v", max_v)

    for k,v in map.items():
        if v>=max_v:
            temp=k
            result=max(result, temp)
            # print(temp)
        
    return result

ans=croack1([1,1,2,3,2, 2, 3, 3,3,3,4])
print(ans)