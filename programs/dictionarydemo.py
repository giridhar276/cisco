
#


#obj = { key:value , key:value , key:value}
book = {"chap1":10 ,"chap2":20 ,"chap3":30}

for v in book.values():
    print(v)

for k,v in book.items():
    print(v)


book = {"chap1":["rita","UK"] ,"chap2":["sita","US"]}

for k,v in book.items():
    print(v[0])

book = {
        "chap1":{"name":"rita","city":"UK"} ,
        "chap2":{"name":"gita","city":"US"} 
        }

for k,v in book.items():
    print(v['name'])


devices = {"device1":["router","host001","manual"],
           "device2":["switch","host002","automatic"]
           }

# host001
# host002