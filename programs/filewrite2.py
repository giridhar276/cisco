

# tradtional way 
fobj = open("clients.txt","w")
fobj.write("cisco\n")
fobj.write("tcs\n")
fobj.write("intel\n")
fobj.close()

# pythonic way
# context manager 
# if any line starts using 'with' keyword... it is called as context manager
# file gets closed automatically when it comes out of indendation
with open("clients.txt","w") as fobj:
    fobj.write("cisco\n")
    fobj.write("tcs\n")
    fobj.write("intel\n")

