###list operations
#Concatenation with + operator
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
print(a+b) #this concatenates two lists
#Results [1, 2, 3, 4, 5, 6, 7, 8]

#Repetition with * operator(broadcasting)
print(a*2) #it gives [1, 2, 3, 4, 1, 2, 3, 4]

#Membership Check
print(2 in a) #it gives true
print(5 not in b) #it gives false

#Operations
#Methods: Mrthods are the function which are compulsarily called by an object
a = [1, 2]
a.append(3) #a is mutable
##list methods
a = [1, 2, 3]
a.append("Hello")
print(a)
#this gives [1, 2, 3, 'Hello']
result = a.append(4)
#this statements appends value to the list 'a' but it does not return anything, i.e. none
print(a)
#it gives [1, 2, 3, 'Hello', 4]
print(result)
#it gives none

#extend
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print(a)
#it gives [1, 2, 3, 4, 5, 6]
#extend() methods also return None type

#insert
a.insert(1, "Hello World")
print(a)
#result [1, 'Hello World', 2, 3, 4, 5, 6]

a.remove(3) #this removes 3 from the list
print(a)
#result [1, 'Hello World', 2, 4, 5, 6]
a.remove("Hello World")
print(a)
#result [1, 2, 4, 5, 6]
##But if we pass the elements not present in the list to the remove then it raises error.
#Built-in functions


