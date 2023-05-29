from estd_connectionnn import estd_connectionn

cursor = estd_connectionn()

id = input("Enter student id: ")

sql = f"""
SELECT * FROM STUDENT WHERE ID = '{id}'
"""

cursor.execute(sql)
result = cursor.fetchone()
print(result)