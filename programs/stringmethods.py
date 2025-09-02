
name = "python programming"
#slicing
# string[start:stop:step]
print(name[0]) #p
print(name[1]) # y
print(name[0:8]) #python p
print(name[2:5]) #tho
print(name[0:8:1])
print(name[8:])
print(name[::]) #python[0:18:1]
print(name[:])
print(name[0:17:2]) #pto rg
print(name[1:17:3]) # yo
print(name[-1])
print(name[-4:-1])
print(name[::-1])

#                             
#p   y   t   h   o   n       p   r   o   g    r    a    m    m    i    n    g
#0   1   2   3   4   4   6   7   8   9   10   11   12   13   14   15   16   17
#                                                 -6    -5   -4    -3    -2   -1



name = "python programming"
print(name.capitalize())
name = name.capitalize()
print("Initial:",name)


print(name.title())
print(name.casefold())
print(name.count('p'))
print(name.center(40))
print(name.center(40,"*"))
print(name.endswith("g"))
print(name.endswith("zg"))
print(name.startswith("p"))
print(name.startswith("z"))
print(name.find("pro")) # if found.. returns starting index of substring
print(name.find("abc")) # if not found.. it returns -1

aname = "I love {} and {}" #template
print(aname.format("Bang","hyd"))
print(aname.format("Delhi","Mumbai"))
print(aname.format("C","C++"))

lang1 = "unix"
lang2 = "java"
print(f"I love {lang1} and {lang2}") # fstring style

print(name.isalnum())
print(name.isupper())
print(name.islower())
print(name.isdigit())

aname = " python  "
print(len(aname))
print(len(aname.strip())) # remove whitespaces at both ends
print(len(aname.lstrip()))
print(len(aname.rstrip()))

print(name.split(" ")) # string to list

data = ['python', 'programming']
print(" ".join(data))  # list to string


name ="python"
# simple if
if name.isupper():
    print("string is upper")

# if-else
name = input("Enter any language :")
if name == "python":
    print("its python")
    print("inside if")
    print("still inside if")
else:
    print("its java")
    print("inside else")
    print("still inside else")

# if-elif-elif-elif-else
name = input("Enter any language :")
if name == "python":
    print("its python")
elif name == "java":
    print("its java")
elif name == "react":
    print("its react")
else:
    print("its some other programming language")

################# program to check whehter substring is existing or not
name = "python programming"
if name.find("pro") != -1 :
    print("substring found")
else:
    print("substring not found")

## simplest way 
if "pro" in name:
    print("substring found")
else:
    print("not found")




#### range(start,stop,step). 
# range(10) : 0 to 9
for val in range(1,11):
    print(val)

for val in range(10,0,-1):
    print(val)
# string
name = "python"
for char in name:
    print(char)
#list
alist = [10,20,30]
for val in alist:
    print(val)
# tuple
atup = (10,20,30)
for val in atup:
    print(val)
#dictionary
book = {"chap1":10,"chap2":20}
for key in book.keys():
    print(key)



#
first = "python"
second = "programming"
print(first + second)

alist =[10,20]
blist = [30,40]
print(alist + blist)

atup = (10,20)
btup = (30,40)
print(atup + alist)

print(first * 3)