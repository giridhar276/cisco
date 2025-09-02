

string = input("Enter any string:") #python
result = ""
#vowels = ["a","e","i","o","u","A","E","I","O","U"]
vowels = "aeiouAEIOU"
for char in string:
    if char in vowels:
        result = result + "*"
    else:
        result = result + char
print(result)