import os
import sqlite3


def execute_query(query, args):
    db_path = os.path.join(os.getcwd(), 'example.sqlite3')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute(query, args)
    connection.commit()
    records = cursor.fetchall()
    return records
