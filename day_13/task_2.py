#from the given list of integer create a number whose digits are the element of list
#A =[4, 2, 3, 1, 2, 5]
#Result =423125

list = [4, 2, 3, 1, 2, 5]
s = ""
for i in list:
    s += f"{i}"
print(s)
