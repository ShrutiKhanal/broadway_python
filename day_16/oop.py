#Creating a class A
class A:
    a = 1 #class attribute

    def __init__(self, b, c): #init is a constructor
        self.b = b  #Instance attribute
        self.c = c  #Instance attribute


    def get_a(self): #This is a behaviour also called as methods
        return self.a

obj1 = A(5, 4) #Creating an object of class A
print(obj1.a)
print(obj1.b)
print(obj1.c)

obj2 = A(10, 15) #Creating an object of class A
print(obj2.a)
print(obj2.b)
print(obj2.c)


###Characterstics of OOP
# 1. Inheritance   #Concpet of child classes
# 2. Encapsulation #Concept of hiding methods and properties(Private, protected, public)
# 3. Polymorphism  #Different form of same function
# 4. Abstraction   #Making only required logic accessible to the end user