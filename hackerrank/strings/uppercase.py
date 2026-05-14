def is_strong_password(password):


    if len(password) < 8:  # change 8 to your required minimum length
        return False

    has_digit = any(c.isdigit() for c in password)
    has_lower = any(c.islower() for c in password)
    
    has_upper = any(c.isupper() for c in password)
  
    has_special = any(c in "!@#$%^&*()-+" for c in password)

    # if has_digit==True:
    #     return False
    
    return  (not has_digit) and has_lower and has_upper and has_special


# Test
pwd = "Abc!abcdefr123"
print(is_strong_password(pwd))

