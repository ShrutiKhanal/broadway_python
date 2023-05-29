import csv
from day_25.estd_connectionnn import estd_connectionn


def insert(student_id, name, age):
    cursor = estd_connectionn()

    sql = f"""
    INSERT INTO STUDENT(ID, NAME, AGE) VALUES ('{id}', '{name}', '{age}')
    """
    cursor.execute(sql)
    print("Student added successfully !!")


with open("student.csv") as cr:
    csv_reader = csv.DictReader(cr)
    for data in csv_reader:
        insert(data['id'], data['name'], data['age'])