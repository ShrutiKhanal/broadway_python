student = {"name": "Jon", "age": 23}

print(all(student)) #Returns True if all the values in the iteration are Truthy. Here Result=> True.
# This is like AND operation

print(all([])) #This is an excecption because it gives True


print(any(student)) #This gives True. any() returns True if any of the elements in an iterable is truthy.
# This is like OR operation.
print(any([])) #this gives false

result =sorted(student) #It sorts the key of the dictionary and return a list
print(result) #['age', 'name']


#Dictionary methods continue
student = {"name": "Jon", "age": 23}
print(student.items()) #it gives dict_items([('name', 'Jon'), ('age', 23)])

print(student.keys()) #it gives list like object of dictionary keys
# result=> dict_keys(['name', 'age'])

print(student.values()) #it gives list like object of dictionary values
#results: dict_values(['Jon', 23])

d = student.fromkeys([1, 2, 3])
print(d) #gives a new dictionary with keys of iterable with common value
#Result= {1: 'Hello', 2: 'Hello', 3: 'Hello'}

d = student.fromkeys([1, 2, 3])
print(d) #Result {1: None, 2: None, 3: None}
