# 3sum


def sub_string(input):
    sub_s="rosy"
    if sub_s in input:
        print("yes")
    # find index
    index = input.find("rosy")
    print(index)



    return 1

# count of substring in a string
#easy way --- input.count(sub_s)

def count_f(input):
    # index=0
    sub_s="rosy"
    count = 0
    index = input.find("rosy")
    # print(F"index ISss {index}") # 0

    while(index!=-1):
        count += 1
        index = index + len(sub_s)
        index=input.find("rosy", index)
    return count

s = "roy is rosy rosy" #11
ans=count_f(s)

print(ans)

# find all substrings of a string
def print_sub(s):
    l=[]
    for i in range(0,len(s)):
        for j in range(i+1,len(s)+1):
            print(s[i:j]) # does ot take last value of j
            l.append(s[i:j])
    return l

ans=print_sub("rosy")
print(ans)

