# check all char of expected are in input

# check all char of expected are in input
# not the corrcet solution 

# print(ord('A'))

def is_strong1_password(s):
    l=[0]*26
    # print(l)
    v=0

    for c in s:
        if c.isalpha():
            v=ord(c.lower())-ord('a')
            # print(v) 
            l[v]+=1
    # print(l)

    for item in l:
        if item==0:
            return False

    return True


input = "the quick brown fox jumps over the lay dog"
print(is_strong1_password(input))










