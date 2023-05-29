#Create a dictionary student with keys id, name, age, department. Take a input from the user,
# which info(id, name, age or department) he wants to access and print the result. Handle the possible excecption.

student = {"id": "24306", "name": "Shruti", "age": 20, "department": "CSIT"}
key = input("Enter the info you want to get:")

try:
    result = student[key]
except KeyError:
    print("Invalid Key")
else:
    print(f"The {key} of the student s {result}")