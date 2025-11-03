# 3sum

# input=daabcbaabcbc, output =dab

def remove_all(input,part):
    start=0
    index=input.find(part)

    while index!= -1:
        input=input.replace(part, '')
        index = input.find(part)


    return input


ans=remove_all("daabcbaabcbc", "abc")
print(ans)

