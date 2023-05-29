##Lambda / Anonymous function
#Lambda functions are the one linear function in python. They don't have name.
# So, they are called as anonymous function.


def addition(a,b):
    return a + b #This is normal function


#This is a lambda function
add = lambda a, b: a + b
print(add(3, 4))


a = [(3, 6), (1, 2), (4, 5), (2, 1)]

a.sort(key=lambda data: data[1])
print(a)



##Higher order functions
#If a function takes another function as a parameter then it is a higher order function
#map(), filter(), and reduce() are the examples of higher order functions



#map() function

a = [1, 2, 3, 4, 5]

def multiple_of_two(data):
    return data * 2

#or

result = map(lambda data: data * 2, a)
print(list(result))


#filter() function = existing iterable bata pick garcha #esko function ma T ki F return garne lekhne

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def get_even_nums(data):
    return data % 2 == 0
#or

result = filter(lambda data: data % 2 == 0, a)
print(list(result))

#reduce() function
from functools import reduce

a = [1, 2, 3, 4, 5] #((((1+2)+3)+4)+5) = 15
result = reduce(lambda x, y: x +y, a)
print(result)