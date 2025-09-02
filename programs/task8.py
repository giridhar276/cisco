

#wrrite a program to reverse a list without list.reverse() and [::-1]


alist = [56,3,65,26,5,74,62,27,94]
revlist = [ ]
for i in alist:
    revlist = [i] + revlist
print(revlist)