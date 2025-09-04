


try:
    fobj = open("clients11111.txt","r")
    #case1: if file is existing ... else block will get executed
    #case2: if file is not existing... except block will ge executed
except Exception as err:
    print(err)
else:
    print(fobj.read())
finally:
    print("end of file operation")
