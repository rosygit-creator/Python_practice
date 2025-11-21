

# count of longest substring in a string with repeating characters-2 loops
def program1(input, c):
    # index=0

    count = 0
    # print(input.count(c))
    for i in range(0, len(input)):
        if c==input[i]:
            count+=1

    return count

s = "aaabbbbefbb"
ans=program1(s, "a")
print(ans)

