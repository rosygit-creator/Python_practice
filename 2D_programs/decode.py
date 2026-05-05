# https://leetcode.com/problems/decode-ways/

# reference
# ASCII value for uppercase 'A'
# ascii_a = 65
# char_a = chr(ascii_a)
# print(f"The character for ASCII value {ascii_a} is: {char_a}")

def board1(b):
    input=[]
    output=""
    n = 65
    input=[0] * 27
    for i in range(1, 27):

        input[i]=chr(n)
        n+=1
    print(input)

    for c in b:
        index=int(c)
        output=output+str(input[index])
    # print(input)






    return output


ans=board1("123")
print(ans)
ans=board1("111222")
print(ans)