#task

a = float(input("Enter the score:"))
if a > 1 or a < 0:
    print("Invalid score")
elif a >= 0.9:
    print("grade A")
elif a >= 0.8:
    print("grade B")
elif a >= 0.7:
    print("grade C")
elif a >= 0.6:
    print("grade D")
else:
    print("grade F")