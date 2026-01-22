# https://leetcode.com/problems/sort-characters-by-frequency/description/

def arrange_by_freq(input):
    map={}
    output=""

    for c in input:
        if c not in map:
            map[c]=1
        else:
            map[c]+= 1
    sorted_items=sorted(map.items(), key=lambda item: item[1], reverse=True)

        # convert back to dict
    sorted_dictionary=dict(sorted_items)
    print(sorted_dictionary)

    for k,v in sorted_dictionary.items():
        output=output+k*v  # prints k as v number of times

    return output

ans=arrange_by_freq("tree")
# ans=word_subsets_all(words1, words2)
print(ans)


