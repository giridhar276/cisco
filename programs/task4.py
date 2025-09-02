
'''
write a program to count how many uppercase , lowercase letters and digits are  in  a string


Enter a string: PyTHon108
Uppercase letters: 3
Lowercase letters: 3
Digits : 3

'''

string = input("Enter any string:")
upper = 0
lower = 0
digit = 0
for char in string:
    if char.isupper():
        upper+=1
    elif char.islower():
        lower+=1
    elif char.isdigit():
        digit+=1

print("No. of uppercase :", upper)
print("No. of lowercase :", lower)
print("NO. of digits    :", digit)