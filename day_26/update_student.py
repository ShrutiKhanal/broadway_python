from day_25.estd_connectionnn import estd_connectionn

def update(id, to_change, changed_value):
    cursor = estd_connectionn()

    sql = f"""
    UPDATE STUDENT SET {to_change} = '{changed_value}' WHERE ID = '{id}'
    """

    cursor.execute(sql)
    print("Student updated successfully !!")
    choice = input("Wish to continue (y/n)? ")
    return True if choice == 'y' else False