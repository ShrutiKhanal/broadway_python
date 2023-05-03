#An emoty set can be created in python with ab built-in function set()

#Sets are the mutable data types in python but the elements of the set must be immutable.

#Sets are unordered datatypes i.e {1, 2} and {2, 1} are same.

s = set() #Creating an empty set
print(s)

s = {2, 4, 6, 6} #A non-empty set
print(s)
s = {1, 2, 2, 3, 4, 4} #It gives {1, 2, 3, 4} because set elements are unique and non-repeated

#s = {[1, 2, 3], 4} #This not possible in set because all set because all the element must be immutable in set but,
# it has a list

##Adding elements in list
s = {1, 2, 3}
s.add(4) #It adds an element to a random position in a set
print(s)

s.update([5, 6, 7]) #We can use update() method to update a set. Update method takes an iterable/sequence as a parameter
print(s) #Result  {1, 2, 3, 4, 5, 6, 7}

#Removing element in set
s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
s.remove(8) #remove method takes value(not index) as a parameter
print(s) #Result: {1, 2, 3, 4, 5, 6, 7, 9, 10}

s.discard(5)
print(s) #Result {1, 2, 3, 4, 6, 7, 9, 10}

#The difference in discard() and remove() method is remove raises an error if the value to be
# remove is not present in the set. But, the discard() method return None if the value to be
# removed is not present in the set

s.pop() #It pops out an element from a random position in set.
print(s)

s.clear() #It clears the set
print(s)


