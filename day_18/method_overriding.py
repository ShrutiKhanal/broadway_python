#task

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self): #this is a instance method
        return f"Person name is{self.name} and age is {self.age}"

class Employee(Person):
    def __init__(self, name, age, salary, designation,):
        self.salary = salary
        self.designation = designation
        super().__init__(name, age)

    def get_details(self):
        print(super().get_details())
        return f"salary is {self.salary} and designation is {self.designation}"

person = Employee("jon", 45, 500, "manager")
print(person.get_details())