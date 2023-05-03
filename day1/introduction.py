### Arithmetic operators

#Addition
a = 1
b = 2
print(a+b) # Here + is addition operator

#Subtraction
a = 5
b = 2
print(b-a) # Here minus is a subtraction operator

#multiplication
print(a*b) # *operator is used for multiplication

#Division
print(a/b) #here / is used for division operation

#Exponent
print(a ** 2) #here ** is 'a' raised to the power 2
#** is used for exponential operation

print(a % 2) #here a is 5. So, remainder of 5/2 is 1

print(a//2) #here // is an operator for floor division that terminates the decimal digits digits. Hence it returns 2


###Relational operators/comparison
a = 1
b = 1
print(a == b) # == is a comparision operator to check whether the values are equal or not. Here it is given True.

a = 5
print(a>b) #it returns false
print(b>a) #it returns true

a = 2
b = 2
print(a >= b)  #it returns true
print(a <= b)  #it returns true

print(a != b)  #it returns false

###Logical operations
#AND
print(True and True) #True
print(True and False) #False
print(False and True) #False
print(False and False) #False

#OR
print(True and True) #True
print(True and False) #True
print(False and True) #True
print(False and False) #False

#NOT
print(not True) #False
print(not False)#True

###Identity operator

# is and is not are the identity check operator

a = 1
b = 1
#here a and b both refers to the same object with value 1
print(a is b) #so it returns True

b = 123
print(a is b) #it returns False becasue b is another object with value 123
print(a is not b) #it gives True.

###Membership operator
ages = [21, 22, 23, 24]
print(21 in ages) #it gives True
print(22 not in ages) #it gives False

print(25 in ages) #it gives True
print(25 not in ages) #it gives False

name = 'Broadway'
print('B' in name) #it gives True

###Assignment operators

a = 1 #"=" is the simplest assignment operator which assigns value from the RHS to the variable in LHS
a = a + 1 #This increase the value od a by 1. But this logic can also be written as following
a += 1 #here += is an assignment operator
a -= 1 #here -= is an assignment operator

###Precendence and Associativity

#Precedence is the rule that determines the priority of operators in  an operation
#Associativity is the rule that determines the priority of operators if one or more operators have the same precedence

#Normally associativity is from left to right but for '**' operator it is right to left

print(2**3**2) #3**2 is evaluated first and the result is raised power to 2.

###comments
"""
 statements 
"""




