a = "Hello World"
print(len(a)) #This returns the length of a sequence /iterable

print(bool(a)) #here a is non-empty string which is Truthy. So it gives True.

print(a[slice(1, 5)]) #slice() function can be used in the string slicing.
# First parameter is start and second parameter is stop.
#Slice(start, stop, step) #step can also be provided as the third parameter

print(type(a)) #this return the type of object inside the function. Here it is string #Result: <class 'str'>

