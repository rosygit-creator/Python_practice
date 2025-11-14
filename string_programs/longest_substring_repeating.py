

# count of longest substring in a string with repeating characters-2 loops
def count_longest_substring(input):
    # index=0
    max_l=0
    count = 1
    for i in range (0, len(input)-1):
        count=1
        # print("inside i")
        for j in range(i+1, len(input)):
            # print("inside j")

            if input[i]==input[j]:
                count+=1
                # print(f"char input[i] is {input[i]}, char {input[j]}, count {count}")
            else:
                if input[i]!=input[j]:
                    # max_l=count
                    break

        max_l=max(count,max_l)

    return max_l

s = "aaabbbbefbb"
# ans=count_longest_substring(s)

# print(ans)

#count of longest substring in a string with repeating characters-1 loop
def count_longest_substring1(s):
    max_l = 1
    count = 1
    for i in range(0, len(s) - 1):
        if s[i]==s[i+1]:
            count+=1
        else:
            max_l=max(count, max_l)
            count=1

    return max_l

s = "aaabbbcccccdd"
ans=count_longest_substring1(s)

print(ans)