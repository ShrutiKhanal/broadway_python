# Opening files in different modes:
# 1. r => Read Mode
# 2. w => Write Mode
# 3. a => Append Mode
# 4. x => Exclusive Write Mode
# 5. b => Binary Mode (rb, wb, r+b, w+b)
# 6. r+ => Read and Write Mode
# 7. w+ => Write and Read Mode
# 8. a+ => Append and Read Mode

filename = "info.txt"

# Write Mode
# fp = open("info.txt", "w")
# fp.write("Hello World") #fp = filepointer
# fp.close()

# Read Mode
# fp = open(filename, "r")
# data =fp.read()
# print(data)
# fp.close()

# Write and Read mode
fp = open(filename, "w+")
fp.write("Python is a high-level language")
fp.seek(0) #moves the file cursor to the very first location of the file
data = fp.read()
print(data)
fp.close()


# fp = open(filename, "r+")
# data = fp.read()
# print(data)
# fp.write("Hello Broadway")
# fp.close()

# Append mode
fp = open(filename, "a")
fp.write("\nI'm learning Python")
fp.close()

# Exclusive Write mode
# fp = open(filename, "x")
# fp.write("Hello World")
# fp.close()

# Context Manager
filename = "message.txt"
with open(filename, "w+") as fp:
    fp.write("Hello World")
    fp.seek(0)
    data = fp.read()
    print(data)

# Append mode
with open(filename, "a") as fp:
    fp.write("\nPython class")


import test1  #Directly importing a module
from test1 import addition #Importing function from a module


from day_20.recursion import message
from day_20 import recursion
recursion.message()
