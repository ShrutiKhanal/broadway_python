#In python (or in any other language) there are three types of errer:
# 1. Syntax error
# 2. Logical error
# 3. Excecption/runtime error


try:
    number = int(input("enter the number:"))

except ValueError:
    print("Please enter the valid number")
except TypeError:
    print("TypeError")
else:
    x = number
    y = number
    summ = (x + y)
    print(summ)
finally:
    print("Finally Executed")

# try:
#     fp = open("student.txt", a)
#     print(fp)
#     a =2
#     print(a)
# except:
#     print("Excecption occured")
# finally:
#     fp.close()