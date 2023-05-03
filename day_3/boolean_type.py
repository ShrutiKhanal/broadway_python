#True and False are the keyword for boolean type in Python
#Logicaloperations, relational operations, identity operations and membership operations returns boolean result

a = 1
b = 2
c = 0
#Logical operations
print(bool(a) and bool(b)) #this gives true
print(bool(a) and bool(c)) #this gives false

print(bool(a) or bool(c)) #this gives True

#relational operations
print(a>b) #False
print(b>a) #True
print(a==b) #False
print(a!=b) #True

#Identity operations
a = 1
b = 1
c = 2
print(a is b) #true i.e 1 eutai object bhayera
print(a is c) #false i.e eutai object haina 2 ra 1 so false

#Membership operations
print(2 in [1, 2, 3]) #True
print(3 not in [1, 2,3]) #False
print('h' in 'hello') #true

#Boolean is subclass of integer type in python. Thus True represents integer 1 and False represents integer 0
#Arithmetic operation sa re possible for Boolean type

print(True + 1) #result: 2(1+1)
print(False + 5) #result: 5(0+5)
print(False * 70) #result: 0(0*70)


#bool() built-in function
#bool() funcction can take any object as parameter and return True and False based on the truthy or falsy nature of the object
#Any non-empty strings, tuples, dictionarym set are truthy in nature. Also, all integers are truthy in nature except 0
print(bool("Hello")) #True
print(bool([1, 2, 3])) #True
print(bool({"name": "Jon"})) #True
print(bool({1, 2, 3})) #True
print(bool(5)) #True
print(bool(-5)) #True

#All empty list, dictionary, set, string(or any empty object) are falsy in nature, 0 and None are also falsy in nature
print(bool(None)) #false
print(bool(0)) #false
print(bool("")) #false
print(bool({})) #false
print(bool([])) #false
print(bool(False)) #false
