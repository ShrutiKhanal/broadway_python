#string formatting using %

m = "Hello I'm %s. I'm %d years old" %("Jon", 45)
print(m) #Result=> Hello I'm Jon. I'm 45 years old

m = "I have Rs. %.2f" %(30.55878)
print(m) #Result I have Rs. 30.56


#String formatting using format() Method
m = "Hello I'm {}".format("Jon")
print(m)

m = "I'm {age} years old".format(age=45)
print(m)

m = "I have {0}, {1} and {2}".format("pen", "pencil", "copy")
print(m) #result I have pen, pencil and copy

m = "I have {1}, {0} and {2}".format("pen", "pencil", "copy")
print(m) #result I have pencil, pen and copy

#if we don't give index and have multiple placeholders then the values are taken in order

m = "I have {}, {} and {}".format("pen", "pencil", "copy")
print(m) #Result= I have pen, pencil and copy