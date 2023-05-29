#Create a function to divide a number by another number. Handle the possible excecption

try:
    number1 = int(input("Enter first number:"))
    number2 = int(input("Enter second number:"))
    print("Division result is:", number1/number2)
except ValueError:
    print("Please enter valid number")
except ZeroDivisionError:
    print("Value cannot be divided by 0")


