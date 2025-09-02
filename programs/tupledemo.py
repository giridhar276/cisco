alist = [10,20,30]
alist[0] = 100
print(alist) # [100,20,30]


atup = (10,20,30)  # tuple
#atup[0] = 100
alist = list(atup) # converting to list
alist.append(40)   # making changes
atup = tuple(alist)# reconverting back to tuple
print(atup)