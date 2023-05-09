### enumerate() function #list bhitra index, value dincha

vowels = ["a", "e", "i", "o", "u"]
for vowel in vowels:
    print(vowel)

for index, vowel in enumerate(vowels):
    print(index)
    print(vowel)

for count, vowel in enumerate(vowels, start=1): #start lekhnu ra sidhai 1 lekhnu is same
    print(count)
    print(vowel)