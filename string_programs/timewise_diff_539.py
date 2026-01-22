# https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/description/
# soluton: https://algo.monster/liteproblems/539
# why a 24 hr count is needed?
from itertools import pairwise

def timewise_diff(input):
    temp_list=[]


    # for time in input:
    # end index is not included in slicing, for loop is needed here
    temp_list=sorted(int(time[:2])*60+int(time[3:]) for time in input)
    temp_list.append(temp_list[0]+1440)

        # temp=input[i].split(":") instead of this, slicing can be done as above

        # print(temp_list)
        # Find the minimum difference between consecutive times
        # pairwise creates pairs of consecutive elements: (a, b), (b, c), (c, d)...

    return min(b - a for a, b in pairwise(temp_list))


#timePoints = ["23:59","00:00"] #1
# ans=timewise_diff(timePoints)
# print(ans)


timePoints = ["23:58", "00:00", "12:30", "23:45"]
ans=timewise_diff(timePoints)
print(ans)