
'''
write a program to reverse a string without using [::-1]

Enter any string:  python
nohtyp
'''

string = input("Enter any string :") #python
revstr = ""
for char in string:
    revstr = char + revstr
print("Strin reverse :", revstr)

