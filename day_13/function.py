#Fucntions are the block of resuable code

#This ia function definition
def addition(a, b):
    print(a+b)

#This are function calls
addition(2, 3)
addition(6, 7)

#Return statement in a function

#if we don't return anything from a function then it returns None by default
#This is a function definition without any return and thus returns None.
def addition(a, b):
    print(a + b)

result = addition(2, 3)
print(result) #Result = None

#This is a function definition with a return. Here it returns sum of the parameters
def addition(a, b):
    return a +b

result = addition(2, 3)
print(result) #Result = 5


#Function Argument
#Python function arguments are of three types
#1. Positional Arguments
#2. Keyword / Default arguments
#3. Arbitary arguments

#Here a, b and c are positional arguments.Positional arguments should be sent compulsorily during the function call
def summ(a, b, c):
    return a + b + c

#Here b is a keyword or default parameter.
result = summ(1, 2, 3)

def summ(a, b = 2):
    return a + b

print(sum(2)) #It is not mandatory to send a default parameter during function call
print(sum(4 , 5)) #Default arguments are only for fallbacks. Default values are overriddern
# if a different value is sent during the function call.