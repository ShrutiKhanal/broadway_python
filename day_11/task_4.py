##

hour = float(input("Number of hours worked:"))
rate = float(input("Rate per hour"))

if hour <= 40:
    print(hour*rate)
else:
    print(40*rate + (hour-40)*rate*1.5)

