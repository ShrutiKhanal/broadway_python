#first 50 even numbers

count = 0
num = 0
while count < 50:
    if num % 2 == 0:
        print(num)
        count += 1
    num += 1

###OR
count = 0
num = 0
while count != 50:
    if num % 2 == 0:
        print(num)
        count += 1
    num += 1