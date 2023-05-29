##functions are objects
#Function can be stored in  data structure
#Function can be passed to another function
#Function can be nested

#Functions can be stored in a variable
def addition (a, b):
    return a + b


print(addition(2, 3))

add = addition
print(add(4, 7))

#Functions can be stored in data structures

data = [1, 2, add, lambda x, y: x + y, addition]
print(data)