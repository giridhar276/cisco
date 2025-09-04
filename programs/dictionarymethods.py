book = {"chap1":10 ,"chap2":20 ,"chap3":30}

#add new key-value to dictionary
book["chap4"] = 40
book["chap5"] = 50
book["chap6"] = 60
print(book)

# display individual value
print(book["chap1"])
print(book["chap2"])
print(book["chap4"])

### display keys
print(book.keys())

for key in book.keys():
    print(key)

## display values
print(book.values())

for value in book.values():
    print(value)


# display key,value at a time
print(book.items())

for k,v in book.items():
    print("key : ",k)
    print("value:",v)

## deleting key-value
book.pop("chap1")   #chap1-10 will be deleted from dictionary
print(book)

## delete last inserted key-value
book.popitem()
print(book)
book.popitem()
print(book)

book = {"chap1":10,"chap2":20}
newbook = {"chap3":30 ,"chap4":40}
finalbook = {**book,**newbook}
print(finalbook)

## existing book will be updated with newbook
book.update(newbook)
print(book)    # will be updated with newbook
print(newbook) # this will remain same




book = {"chap1":["rita","UK",200] ,
        "chap2":["gita","US",300] }
