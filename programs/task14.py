'''
data = ["Alice", "", None, "Bob", "Carol", "", None]

Write a program to replace all None or empty strings in a list with 'NA'.

output:
["Alice", 'NA', 'NA', "Bob", "Carol", 'NA', 'NA']
'''

data = ["Alice", "", None, "Bob", "Carol", "", None]
output = []
for item in data:
    if item == ""  or item == None:
        output.append("NA")
    else:
        output.append(item)
print(output)


data = ["Alice", "", None, "Bob", "Carol", "", None]
for index in range(0,len(data)):
    if data[index] == "" or data[index] == None:
        data[index] = "NA"
print(data)