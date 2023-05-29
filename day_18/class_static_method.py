# important for interview 
class Person:
    __department = "CS" #class attribute

    def __init__(self, name, age):
        self.name = name #instance attribute
        self.age = age

    @classmethod #class method le class as a parameter lincha
    def set_department(cls, department):
        cls.__department = department

    @classmethod
    def get_department(cls):
        return cls.__department


# print(Person.department) #Can't access from outside the class because it is a private class attribute
print(Person.get_department())
Person.set_department("Mathematics")
print(Person.get_department())