#if...elif...elif..else ladder
a = 5
b = 4

#In this example both the conditions are satisfied and the statements are executed
if a == 5:
    print("First print 5")

if a == 5:
    print("Second print 5")
else:
    print("no file ")

#In this example, we have used if...elif...else ladder. So, if one of the condition is
# met then other condition are not checked
if a == 5:
    print("First print 5")
elif a == 5:
    print("Second print 5")
else:
    print("no file ")


if a > b:
    print(a)
elif b == a:
    print(b)
elif b > a:
    print(a)
else:
    print(b)


#Nested if

a =(1, 2, 3, 4)
if a:
    if type(a) == list:
        print(a)
    else:
        print("It is not a list")
else:
    print("'a' is empty")