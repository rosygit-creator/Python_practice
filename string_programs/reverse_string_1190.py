def reverse_string(s):
    st=[]
    output=""

    for c in s:
        output=""
        if c==')':
            while st[-1]!='(':
                output=output+st.pop()
            # print("output", output)
            st.pop() # pop the (
            st.extend(output) # add the reverse order/ whatever is popped back to st 
            print("output1", st)
        else:
            st.append(c)
            # print("st else is ", st)

    return output

s = "(u(love)i)"
ans=reverse_string(s)
print("ans", ans)



