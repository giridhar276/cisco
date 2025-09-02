

string=input("Enter the password : ")
up=0
lw=0
dg=0
min=8
count=len(string)
if(count>=min):
    for char in string:
        if char.isupper():
            up=up+1
        if char.islower():
            lw=lw+1
        if char.isdigit():
            dg=dg+1
print(up)
print(lw)
print(dg)
if up>=1 and lw>=1 and dg>=1:
    print("valid")
else:
    print("Invalid")