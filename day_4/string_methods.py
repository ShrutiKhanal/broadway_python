m = "hello world"
print(m.capitalize()) #result : Hello world
print(m. title()) #result: Hello World
print(m.upper()) #result: HELLO WORLD
print(m.lower()) #Result: hello world

result = m.split() #result= ["hello", "world"]. Splits from a space
print(result) #this gives ['hello', 'world']

result = m.split('e') #splits from 'e'. Result ['h', 'llo world']
print(result)
result = m.split('o') #result ['hello', 'w', 'rld']
print(result)

##Join
message = ["Hello", "World"]
" ".join(message) #this joins the list with a space("") and returns "Hello World"
"+".join(message) #Result 'Hello+World'


#Find and replace
m = "Hello World"
result = m.find("Wo") #'Wo' in the string is at 6th position. Result => 6
print(result)

result = m.find("Woo") #'Woo' is not in the present list. It gives -1
print(result)

result = m.replace("World", "world") #Replace 'World' in the string to 'world'.
print(result) #result=Hello world
