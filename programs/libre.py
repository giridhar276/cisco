
import re

def search_demo():
    #re.search: find first occurrence (case-insensitive)
    text = "I love python and pythonprogramming"
    m = re.search('python', text)
    if m:
        print("Match found")
    else:
        print("No match")

def findall_demo():
    # re.findall: get all matches
    text = "Order 12, item 345 and 6 extras"
    nums = re.findall('\d+', text)
    print("Digits found:", nums)

def sub_demo():
    # re.sub: replace pattern with text
    messy = "Too    many     spaces"
    clean = re.sub('\s+', ' ', messy)
    print("Before:", messy)
    print("After :", clean)

search_demo()
findall_demo()
sub_demo()
