from estd_connectionnn import estd_connectionn

# def exit_message():
#     print("Thank you")
cursor = estd_connectionn()

id = input("Enter student id: ")
to_change = input("What do you want to change? (name / age): ")
# if to_change.lower() not in ["name", "age"]:
#     print("Invalid input")
#     exit_message()
# else:
changed_value = input(f"Enter new {to_change}: ")
# name = input("Enter student name to be changed: ")
# age = int(input("Enter student age to be changed: "))

sql = f"""
UPDATE STUDENT SET {to_change} = '{changed_value}' WHERE ID = '{id}'
"""

cursor.execute(sql)
print("Student updated successfully !!")