# Example 1:
#
# Input: s = "0110111"
# Output: 9
# Explanation: There are 9 substring in total with only 1's characters.
# "1" -> 5 times.
# "11" -> 3 times.
# "111" -> 1 time.

def count_1_substring(input):
    sub_string=[]
    count=0
    temp=''

    for i in range(0, len(input)):
        for j in range(i+1, len(input)+1):
            # print(input[i:j])
    # print(sub_string)
            temp=input[i:j]

            # this code is alo working
            # if is_all_1(input[i:j]):
            #     count+=1


            if all(c=='1' for c in temp):
                count += 1

    return count

def is_all_1(s1):

    return all(c=='1' for c in s1)


ans=count_1_substring("0110111")
print(ans)

