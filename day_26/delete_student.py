from day_25.estd_connectionnn import estd_connectionn


def delete(id):
    cursor = estd_connectionn()
    if id == 'a':
        sql = """
            DELETE FROM STUDENT
        """
        cursor.execute(sql)
        print("All data deleted successfully !!")

    else:
        sql = f"""
        DELETE FROM STUDENT WHERE ID = '{id}'
        """
        cursor.execute(sql)
        print("Student deleted successfully !!")

    choice = input("Wish to continue (y/n)? ")
    return True if choice.lower() == 'y' else False