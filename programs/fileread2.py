
#method1: reading line by line
with open("data.txt","r") as fobj:
    for line in fobj:
        print(line.strip())

#method2: using fobj.readlines() -----> list
with open("data.txt") as fobj:
    print(fobj.readlines())

# method3 using fobj.read(). --> will return string
# not suggested for bigger files
with open("data.txt") as fobj:
    print(fobj.read()) # reading whole file to a string


# method4 : using csv library
# easy way to process dat
import csv
with open("data.txt") as fobj:
    reader = csv.reader(fobj)
    for line in reader:
        print(line)
