#Take two number as input and add those numbers. Handle the possible excecption


try:
    number1 = int(input("Enter the first number:"))
    number2 = int(input("Enter the second number:"))

except ValueError:
    print("ValueError! Please enter the valid number")
else:
    summ = number1 + number2
    print(summ)
finally:
    print("Program Executed!!")

