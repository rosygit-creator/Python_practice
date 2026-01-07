

def check_char_order(input):
    flag=True

    for i in range(1, len(input)):
        if input[i].lower()<=input[i-1].lower():
            return False

    return True


ans=check_char_order("abcde")
assert ans==True

ans=check_char_order("aBc")
assert ans==True, "not true"

# ans=check_char_order("aBca")
# assert ans==True, "not true"


ans=check_char_order("aac")
assert ans==True, "not true1"