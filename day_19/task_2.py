# Create a class circle with an attribute radius. Create two objects of circle c1 and c2.
# Add the radius of the circle and print the result

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def total_radius(self, object):
        return self.radius + object.radius

    def is_greater(self, object):
        if self.radius > object.radius:
            return True
        return False

    def __gt__(self, object): #dunder method or the magic method __gt__
        return self.radius > object.radius

    def __add__(self, object):
        return self.radius + object.radius


c1 = Circle(10)
c2 = Circle(4)
print(c1.radius + c2.radius)

print(c1.total_radius(c2))

if c1.radius > c2.radius:
    print("c1 is greater")
else:
    print("c2 is greater")

print(c1.is_greater(c2))
print(c2.is_greater(c1))

print(c1.__gt__(c2))
print( c1>c2 )

print(c1 +c2)