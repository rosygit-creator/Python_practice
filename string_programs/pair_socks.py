def pair_socks(a):
    map={}
    l=[]
    q=0

    for c in a:
        map[c]=map.get(c,0)+1

    for k,v in map.items():
        pair_count=v//2
        l.append([k,pair_count])

    return l

bill=[1,2,1,2,1,3,2,2,3,4,3,3,3,3]
ans=pair_socks(bill)
print(ans)



