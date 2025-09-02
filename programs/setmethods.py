

aset = {10,10,10,20,30,30,30}
print(aset)
bset = {30,30,30,40,40,40,50}
print(bset)
aset.add(10)
print("set:",aset)
aset.add(40)
print("set:",aset)

print(aset.union(bset))
print(aset.intersection(bset))
print(aset.difference(bset)) # {10,20,30,40} - {30,40,50}
print(aset.issuperset(bset))
print(aset.issubset(bset))