#encapsulation is the concept of making the attributes private or public or protected


class Vehicle:
    def __init__(self, color, doors, milage):
        self.color = color #this is a public attribute
        self._doors = doors #using single underscore '_' -> this is protected attribute
        self.__milage = milage #this is a private attribute

    def get_milage(self):
        return self.__milage

    def set_milage(self, milage):
        self.__milage = milage

#Public attributes are accessible from outside the class
car = Vehicle('red', 4, 50)
print(car.color) #this is getting value
car.color = 'blue' #this is setting the value
print(car.color)

###Protected attributes are also accessible from outside the class but not recommended
print(car._doors) #this is setting value
car._doors = 2 #this is getting value.It is possible for protected members
print(car._doors)

###Private members are not accessible from outside the class
# print(car.__milage)
# car.__milage = 70 #this is not possible for private members

print(car.get_milage())
car.set_milage(40)
print(car.get_milage())



print(dir(car))

print(car._Vehicle__milage) #private access garna #This is termed as Name Mangling