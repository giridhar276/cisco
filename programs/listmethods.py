



alist = [45,67,3,67,3,7,15,75]

print("After appending:",alist)
alist.extend([94,45,6]) # list.extend(iterable)

print("After extending:",alist)
alist.insert(1,100)  # list.insert(where,what) # list.insert(index,value)
print("After inserting:",alist)


alist.pop(3)   #list.pop(index) # value at that index is removed
print("After pop operation :",alist)
####validating existing or not
if 200 in alist:
    alist.remove(200)
    print("After remove :",alist)
else:
    print("value not found")

print(alist.count(10))

alist.reverse()
print("Reverse :",alist)
alist.sort() # ascending order
print("After sorting:",alist)
alist.sort(reverse=True)
print("in descending order:",alist)