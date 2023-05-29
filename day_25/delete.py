from estd_connectionnn import estd_connectionn

cursor = estd_connectionn()

id = input("Enter student id: ")

sql = f"""
DELETE FROM STUDENT WHERE ID = '{id}'
"""

cursor.execute(sql)
print("Student deleted successfully !!")