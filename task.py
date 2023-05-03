a = [(4, 12, 5), (6, 1), (11, 12), (6, 7, 8)]

def get_last_item(data):
    return data[-1]  #last value dina-1 use gareko

a.sort(key=get_last_item)
print(a)


#task2
pi = 3.14
radius = float(input("radius of circle:"))
area_of_c = pi * radius ** 2
print("area of circle is:", area_of_c)

#task 3
pi = 3.14
radius = float(input("radius of circle:"))
circumference_of_c = 2* pi * radius
print("circumference of circle:", circumference_of_c)

#task 4
length = float(input("length of regtangle:"))
breadth = float(input("breadth of rectangle:"))

area = length * breadth

print("area of rectangle with length & breadth", area)

#task
list = [5, 2, 3, 5, 3, 2, 3, 3, 1, 4]
number = int(input("Enter the number to find frequency: "))

print(list.count(3))
