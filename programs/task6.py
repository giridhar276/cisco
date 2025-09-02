# Read password
pw = input("Enter any password: ")  #Pass1234t
# Flags
has_upper = False
has_lower = False
has_digit = False

if len(pw) >= 8: 
    for ch in pw: 
        if not has_upper and ch.isupper():  
            has_upper = True
        elif not has_lower and ch.islower():
            has_lower = True
        elif not has_digit and ch.isdigit():
            has_digit = True
        if has_upper and has_lower and has_digit:
            break

if len(pw) >= 8 and has_upper and has_lower and has_digit:
    print("Valid")
else:
    print("Invalid")

