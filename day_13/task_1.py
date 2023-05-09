##delete all the occurance of a specified character in a given string
#input = "a"
#output=

s = "All the occurrence of specified character in a given string"
new_s = ""
char = input("Enter the character:")
for i in s:
    if i.lower() == char.lower():
        continue
    new_s += i

print(new_s)
