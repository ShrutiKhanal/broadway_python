from datetime import datetime

import day_12.loops


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, year): #this is also called factory method
        age = datetime.today().year - year
        return cls(name, age)

    @staticmethod
    def message(d):
        if d<20:
            return "It is a short distance"
        return "It's way too long"

p1 = Person("Jon", 25)
print(p1.age)
p2 = Person.from_birth_year("Jane", 2002)
print(p2.age)

print(Distance.message(45)) #calling static method using class
print(d1.message(16)) #calling static method using an object
