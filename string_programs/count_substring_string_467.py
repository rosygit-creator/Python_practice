# https://leetcode.com/problems/unique-substrings-in-wraparound-string/description/

def arrange_by_freq(input):
    flag=False
    maxlen=1
    count=1

    for i in range(1, len(input)):

        diff=abs(ord(input[i])-ord(input[i-1]))

        if diff==1 or diff==25:
            flag=True
            count += 1

        else:
            flag=False

            count = 1

            break
        # count+=1
        maxlen=max(maxlen, count)




    return maxlen

ans=arrange_by_freq("a")
ans=arrange_by_freq("zab")
ans=arrange_by_freq("ab")
ans=arrange_by_freq("zaab")

# ans=word_subsets_all(words1, words2)
print(ans)


