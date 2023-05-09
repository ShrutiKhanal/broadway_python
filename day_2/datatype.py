###mutable and immutable

#mutable objects are those objects whose value can be changes even after its creation

#immutable objects are those objects whole value can't be changed once it is created

#Interge, Float, Boolean, Tuples, Strings are immutable data types in python
#List, Dictionary and Srts are the mutable data types in python

a = (1, 2, 3) #immutable type
b = [1, 2 ,3] #mutable types

b[1] = 5 #this is possible as list is mutable type
print(b)

#a[1] = 5 #this is not possible


