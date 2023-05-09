###Iteration in dictionary

student = {"name": "Jon", "age": 45, "department": "cs"}
for key in student:
    print(key) #This gives key of the dictionary 'name', 'age', 'department'


values = student.values()
for value in values:
    print(value)

#OR
for value in student.values():
    print(value) #This gives values of the dictionary 'Jon', 45, 'cs'

for key in student.keys():
    print(key) #this gives 'name', 'age', 'department'

for key, value in student.items(): #gives key value pair
    print(key)
    print(value)