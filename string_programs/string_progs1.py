
#First unique element in string


def first_unique(input):
    flag=True


    for i in range(0,len(input)):
        flag=False
        for j in range(0, len(input)):
            if i!=j and input[i]==input[j]:
                flag=True
                break

        if flag==False:
            return input[i]

def distinct_all(input):
    set1=set(input)



    return set1





# First unique element in string
s = "aabeee"
# ans=first_unique(s)
# print(ans)

# fin all distict char in string
ans=distinct_all(s)
print(ans)

