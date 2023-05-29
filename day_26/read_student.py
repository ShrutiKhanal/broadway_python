from day_25.estd_connectionnn import estd_connectionn


def read(student_id):
    cursor = estd_connectionn()

    sql = f"""
        SELECT * FROM STUDENT WHERE ID = '{student_id}'
    """

    cursor.execute(sql)
    result = cursor.fetchone()
    print(result)
    choice = input("Wish to continue (y/n)? ")
    return True if choice == 'y' else False