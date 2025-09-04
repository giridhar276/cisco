
# write operation
# if path is not mentioned .. file gets created in present directory
fobj = open("clients.txt","w")


fobj.write("cisco\n")
fobj.write("tcs\n")
fobj.write("intel\n")

fobj.writelines(["oracle","microsoft","google\n"])

for val in range(1,10):
    fobj.write( str(val) + "\n")

name = input("Enter your name :")
fobj.write(name + "\n")

fobj.close()