##strings in python are of immutable type.

# We can create an empty string using str() built -in function or using empty, single or double quotes

example = "" #empty string using double quotes
print(example)
example = '' #empty string using single quotes
print(example)
example = str() #empty string
print(example)

example = "Hello World" #It is a valid string
#example = 'Hello World"  #It is invalid string

#Escape sequences
#Escape Sequence / characters are the strings in python which supresses the usual meaning of a chaarcter and gives
#a new meaning

example = 'I\'m learning python' #here \' is an esacpe character
print(example) #result I'm learning python

example = "Path to my file is D:\\Project\\broadway" #here \\ is an escape character
print(example)

example = "Hello\nWorld" #here \n is anew line escape character
print(example)

example = "Hello\tWorld" #'t is an escape character for tab
print(example)

example ="Hello\bWorld" #here b\ is an escape character for backspace
print(example) #result HellWorld

##Triple quoted string
example = '''
Example1
'''
print(example) #example with triple single quotes

example = """
Example2
Example 
"""
print(example) #example with triple double quotes

example = """
I'm learning python 
"""
print(example)
#we do not need to use escape characters for single\double quote in triple quoted string

"""
Function to calculate difference. We can treat this as multiline comment 
"""

def fxn(a, b):
    return a-b


##Indexing and Slicing in string
# string Indexing and slicing is similar to list slicing and indexing

message = "Hello Wolrd"
print(message[3]) #this gives 'l'
print(message[6]) #this gives 'W'
print(message[-2]) #negative indexing is also possible. It gives 'l'

print(message[1:7]) #this gives 'ello W'
print(message[1:-3:2]) #this gives 'el '
print(message[-7:-3]) #this gives 'o Wo'
print(message[-3:-7]) #this gives '' empty string

##String doesn't support item assignment because it is immutable
message = "Hello"
#message[1] = "E" #this is not possible