# https://leetcode.com/problems/interleaving-string/

# reference
# ASCII value for uppercase 'A'
# ascii_a = 65
# char_a = chr(ascii_a)
# print(f"The character for ASCII value {ascii_a} is: {char_a}")

from itertools import zip_longest

def interleave_string(s11,s22,s33):

    for c1, c2 in zip_longest(s11,s22):
        if s33.find(c1) > -1:

            s33=s33.replace(c1, '') # outout of replace has to be always assigned to a string

        if s33.find(c2) > -1:
            s33=s33.replace(c2, '')







    return s33

ans=interleave_string("aa","bb","abab")
assert len(ans)==0

ans=interleave_string("aabcc","dbbca","aadbbbaccc")
assert len(ans)==0

# print(len(ans))