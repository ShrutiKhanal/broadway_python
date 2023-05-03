#Tuple has two methods index() and count()

t = (0, 1, 2, 3, 4)
print(t.index(4))
print(t.count(3))

t = (1, 1, 2, 2, 2, 2)
print(t.count(2))

#Built-in function

t = (1, 2, 3, 4)
result = sum((1, 2, 3, 4))
print(result) #this gives 10

result = max(t)
print(result) #this gives 4

result = min(t)
print(result) #this gives 1

t = (5, 2, 4, 1, 10, 12, 9)
print(sorted(t)) #this gives [1, 2, 4, 5, 9, 10, 12]
print(sorted(reverse=True)) #this gives []

result = (reversed(t))
print(list(result)) #this reversed the sequence. This is not descending order sorting