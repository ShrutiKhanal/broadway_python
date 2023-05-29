##List comprehension
# List Comprehension is the short and elegan pythonic way to create a list

a = []
for i in range(10):
    a.append(i)

print(a)

b = [ i for i in range(10)] #this is a list comprehension
print(b)

b = [i for i in range(20) if i % 2 == 0]
print(b)



###Dictionary comprehension
student = [("name", "Jon"), ("age", 45), ("department", "CS")]
#without dictionary comprehension

d = {}
for k, v in student:
    d.update({k: v})
print(d)

#With dictionary comprehension
d = {k:v for k, v in student}
print(d)

d = {k:v for k, v in student if v!= "Jon"}
print(d)

