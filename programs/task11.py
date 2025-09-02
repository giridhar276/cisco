
'''
write a program to filter words longer than 4 letters

words = ["python","unix","java","oracle"]

output:
["python","oracle"]
'''
words=["python","unix","java","oracle"]
a=[]
for i in words:
    if len(i)>4:
        a.append(i)
print(a)

