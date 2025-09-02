
'''
write a program to remove all the occurences of 10 in the given list
alist = [56,56,34,62,6,10,10,10,54,72,74,27,57,67,10,10,10,10]

output:
[56,56,34,62,6,54,72,74,27,57,67]
'''


alist = [56,56,34,62,6,10,10,10,54,72,74,27,57,67,10,10,10,10]
getcount = alist.count(10)
for val in range(0,getcount):
    alist.remove(10)
print("updated list:",alist)