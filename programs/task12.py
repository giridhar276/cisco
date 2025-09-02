'''
Write a program to join corresponding strings from two lists.

first = ["Good", "Data", "Machine"]
second = ["Morning", "Science", "Learning"]

Output:
Good Morning
Data Science
Machine Learning
'''


first = ["Good", "Data", "Machine"]
second = ["Morning", "Science", "Learning"]


for index in range(0,len(first)):
    final = first[index] + " " + second[index]
    print(final)