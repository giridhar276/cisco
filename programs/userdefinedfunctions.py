# fixed aguments
def display(a,b):
    print(a,b)
display(10,20)

# default arguments
def display(a = 0,b = 0,c = 0):
    print(a,b,c)
display()         # 0  0 0
display(10)       # 10 0 0
display(10,20)    # 10 20 0
display(10,20,30) # 10 20 30


#keyword arguments
def display(b,a,c):
    print(a,b,c)
display(c=30,a=10,b=20)

# variable length arguments
# if any object begins with * , it is treated as tuple
def display(*data):
    print(data)
    for val in data:
        print(val)
display(10,20,30,40,50,12,23,45,65,4,67,43,56,34,5,3,657,3,56,34,56,43,5,43,4)