
'''
write a progarm to count character frequencies:
Enter a string :  hello

h : 1 time
e : 1 time
l : 2 times
o : 1 time
'''

string = input("Enter any string:") #hello
## {"h","e","l","o"}
for char in set(string):   
    print(char,string.count(char),"times")

