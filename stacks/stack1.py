def stack1(s1):
    print(len(s1))
    while s1:  # or len(s1)>0
        s1.pop()
    print(s1)

    s1.append(5)
    s1.append(6)
    print(s1)



    return



a=[2,3,4]
stack1(a)