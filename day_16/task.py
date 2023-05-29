class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14 * self.radius ** 2

    def change_radius(self, radius): #Method to set value
        self.radius = radius

circle1 = Circle(5)
area = circle1.get_area()
print("Area of circle is", area)
circle1.change_radius(2)
print(circle1.get_area()) #get attribute of the object

circle2 = Circle(3)
print(circle2.get_area()) #get attribute of the object
circle2.change_radius(6)
print(circle2.get_area()) #get attribute of the object

circle1.radius = 50 #Setting value to obj(circle1)
print(circle1.get_area())

circle2.radius = 50 #Setting value to obj(circle2)
print(circle2.get_area())