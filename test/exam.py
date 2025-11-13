# Example 1:
#
# Input: s = "consumption required part '1234-00-A' with qtty '1' & consumption required part '1235-00-A' with qtty '2'"
# friday is today


def value(input,part):
    index=input.find(part)
    if index> -1:

        for i in range(index+1, len(input)):
            output=output+input[i]
            if input[i]=="'":
                break










value(" input string", "'")
# ["1234-00-A","1"]
# ["1235-00-A","1"]




def reverse_string(input):
    temp=input.split(" ")
    # print(f"output:{output}")
    output = temp[::-1]
    print(f"output:{output}")


ans=reverse_string("today is friday")
print(ans)

