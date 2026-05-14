def is_strong_password(s, k):
    # print(len(s))
    if k==len(s):
        return s
    # counterclockwise or left rotate this works
    result=""
  
    # if k <len(s):
    #     result=s[k:] + s[:k]

    # clockwise or right rotate

    result=s[len(s)-k:] + s[0:len(s)-k]
    
    # return s[-k:] + s[:-k]  this works
    return result

# Test
pwd = "abcdefghijklmnopqrstuvwxyz"
print(is_strong_password(pwd,2))



