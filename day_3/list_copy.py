#There are two types of copy for the Python objects
#Shallow Copy
#Deep Copy

a = [1, 2, 3]
b = a #this incerases the reference count of [1, 2, 3]. But it is not actual copy

b.append(4)
print(b)
print(a)
#this appends the value 4 in both a and b because they both refer to the same object[1, 2, 3]

b = a.copy() #this makes a shallow copy of a and assigns it to b

#now if we append a value to b, then it doesnot change 'a'
b.append(5)
print(b)
print(a)

#But the case is quite different if the list has a mutable object as an element
a = [[1, 2, 3], 4]
b = a.copy()
b[0][1] = 5
print(b) #result [[1, 5, 3], 4]

#but this also change in variable 'a' even if 'b' is the copy of 'a'
print(a) #result [[1, 5, 3], 4].
#this happened becuase b is only a shallow copy of 'a'

from copy import deepcopy
b = deepcopy(a)
b[0][1] = 2
print(b) #result [[1, 2, 3], 4]
print(a) #result [[1, 5, 3], 4] #this doesnot change value in variable 'a'