from estd_connectionnn import estd_connectionn

cursor = estd_connectionn()

cursor.execute("DROP TABLE STUDENT")

sql = """
CREATE TABLE STUDENT (
    ID CHAR(20),
    NAME CHAR(20),
    AGE INT
)
"""

cursor.execute(sql)
print("Table Created Successfully !!")