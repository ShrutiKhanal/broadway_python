from estd_connectionnn import estd_connectionn

cursor = estd_connectionn()

id = input("Enter student id: ")
name = input("Enter student name: ")
age = int(input("Enter student age: "))

sql = f"""
INSERT INTO STUDENT (ID, NAME, AGE) VALUES ('{id}', '{name}', {age}) 
"""

cursor.execute(sql)
print("Student added successfully !!")