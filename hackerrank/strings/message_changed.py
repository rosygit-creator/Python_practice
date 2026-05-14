def is_strong_password(s):

    count=0
    i=0
    expected="SOS"
    for i in range(0, len(s)):
        if s[i] != expected[i%3]:
            count+=1
        
    

    return count

# Test
pwd = "TOTTOTSOSTOT"
print(is_strong_password(pwd))



