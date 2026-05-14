# check all char of expected are in input
from collections import Counter
# # not the corrcet solution 
# def is_strong_password(s, e):
#     map={}

#     for c in s:
#         map[c] = map.get(c, 0) + 1

#     for c1 in e:
#         if c1 not in map or map.get(c1)==0:
#             return False


#     return True

# # Test
# input = "hackerrrsssnkkk"
# expected='hackerrankkkkk' # returns true expected false
# print(is_strong_password(input, expected))


# check all char of expected are in input
# not the corrcet solution 
def is_strong1_password(s, e):
    print("s", Counter(s))
    print("e", Counter(e))

    if Counter(e)<=Counter(s):
        # print("no")
        return True
    return False

# Test
input = "hackerrrsssnkkk"
expected='hacker' # returns true expected false
print(is_strong1_password(input, expected))










