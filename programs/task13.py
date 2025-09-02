'''
Write a program to get all unique words from a list of sentences.

sentences = ["hello world", "hello python", "data world"]

output:
["hello","world","python","data","world"]


'''

sentences = ["hello world", "hello python", "data world"]
uniquelist = list()
for item in sentences:
    output = item.split(" ")
    uniquelist.extend(output)
print(set(uniquelist))


sentences = ["hello world", "hello python", "data world"]
string = " ".join(sentences)
mylist = string.split(" ")
print(set(mylist))