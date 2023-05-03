#List are the mutable datatypes in python

#Empty list can be created using built-in list() function
a = list() #this gives empty list 'a'
b = [] #empty list can also be created in this way

c = [1, 2, 3] #this is a non-empty list

#List are heterogenous datatypes. That means it can have the elements of different datatypes

c = [1, 'Hello', [5, 6, 7], (1,2)] #List with multiple datatypes
print(c)

###Accessing list elements
#List elements can be accessed with indexing and slicing
#List indexing starts from 0 for forward indexing and -1 for backward indexing

a = [1, "Hello", "World",5.0, [4, 5, 6], 5]
print(a[0]) #this gives 1
print(a[-1]) #negative index starts from -1. So, it gives 5

print(a[4])  #this gives [4, 5, 6]
print(a[-5]) #this gives "Hello"

print(a[4][1]) #this gives 5 from the nested list

#print(a[6]) #it gives list index out of range (Index error)

#We can assign item in any particular index of a list
a[2] = 10 #this changes value at second index of list to 10

##Slicing
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a[:]) #this gives exactly the same list
print(a[:6]) #this include elements from 0 to 5. 6 is excluded
#Result [0, 1, 2, 3, 4, 5]
print(a[0:6]) #this is same as above
#above[:6]
print(a[5:]) #this include elements from fifth index to last
#result [5, 6, 7, 8, 9, 10]

print(a[1:8])
#result [1, 2, 3, 4, 5, 6, 7]

print(a[1:6:2])
#this jumps 1 steps for every elemnts from 1 to 7

##Negative slicing
print(a[:-4])

#this gives elements from 0 index to -5th index : [0, 1, 2, 3, 4, 5, 6]

print(a[-5:])
#this gives elements from -5th index to the last : [6, 7, 8, 9, 10]

print(a[-6:-2])
#this gives elements from -6th to -3rd index : [5, 6, 7, 8]

print(a[-6:-8])
#this gives []


