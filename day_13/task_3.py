#palindrom or not
#treating n as a string
n = input("enter a number:")
reversed = n[::-1]
print("Palindrome") if n == reversed else print("Not palindrome")

#treating n as integer
n = int(input("enter a number:"))
b = n
reverse = 0
while n != 0:
    remainder = n % 10
    reverse = reverse * 10 + remainder ##3
    print(reverse)
    n = n // 10

print("Palindrome") if reverse == b else print("Not palindrome")