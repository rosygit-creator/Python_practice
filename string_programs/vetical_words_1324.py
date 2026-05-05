#  https://leetcode.com/problems/print-words-vertically/description/

# Input: s = "HOW ARE YOU"
# Output: ["HAY","ORO","WEU"]

def reverse_string(s):
    temp=[]
    temp=s.split()
    max_len= max(len(t) for t in temp)
    output=""
    l=[]

    for i in range(0, max_len):
        output=""
        for item in temp:
            if i <len(item): 
                output=output+item[i]
        # print(item[i])
        l.append(output)
    return l

s = "HOW AR YOU"
ans=reverse_string(s)
print("ans", ans)