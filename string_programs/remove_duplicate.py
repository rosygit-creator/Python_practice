# https://leetcode.com/problems/remove-duplicate-letters/


def remove_duplicate1(input):
    o=""
    for c in s:
        if c not in o:
            o=o+c
    return o


def remove_duplicate2(input):
    o=""
    set1=set(input)
    # print(f"output {set1}")
    o=o.join(set1)
    print(f"output {o}")
    return o



s = "aabceeedw"
ans=remove_duplicate1(s)
print(ans)

s1 = "aabceeedw"
ans1=remove_duplicate2(s1)
print(ans1)

