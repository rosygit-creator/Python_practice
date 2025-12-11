
#input:aaabeeeedfg
#output:a3b1e4d1f1g1


def countchar(input):
    map={}
    output=""

    # below is another way to add items in a dict
    # for e in input:
    #     if e in map:
    #         map[e]+=1
    #     else:
    #         map[e]=1

    for e in input:
        map[e]=map.get(e,0)+1

    for k,v in map.items():
        # print(k)
        # print(v)
        output=output+k+str(v)





    return output


ans=countchar("aaabeeeedfg")
print(ans)

