
# traditional way
# fixed aguments
def display(a,b):
    c = a + b
    return c
total = display(10,20)
print(total)

# pythonic way
#lambda or ananymous function or nameless function
#lamdba : lambda is the replacement of single liner function only
#syntax:  functioname = lambda variables:expression

display = lambda x, y : x + y
total = display(10,20)
print(total)