s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

s = s1.union(s2) #It gives union of two sets
print(s)

s = s1.intersection(s2) #It gives intersection of two sets
print(s)

s1.isdisjoint(s2) #s1 and s2 are not a disjoint set as they have common elements {4, 5}. So, it gives False.

s = s1.symmetric_difference(s2) #This is a complement of s1 interdection of s2
print(s)
#Result {1, 2, 3,  6, 7, 8}

s1.symmetric_difference_update(s2) #This updates the symmetric difference of s1 and s2 to s1
print(s1) #result {1, 2, 3, 6, 7, 8}

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
print(s2.issubset(s1)) #True
print(s1.issuperset(s2)) #True
print(s2.issuperset(s1)) #False


##Bitwise operator in set operations
s = s1 | s2 #Union same as s1.union(s2)
print(s)
s = s1 & s2 #Intersection same as s1.intersection(s2)
print(s)
s = s1 - s2 #Difference same as s1.difference(s2)
print(s)
s = s1 ^ s2 #Symmetric difference
print(s)