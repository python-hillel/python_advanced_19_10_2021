import os
import sqlite3


def execute_query(query):
    # db_path = os.path.join(os.getcwd(), 'example.sqlite3')
    connection = sqlite3.connect('example.sqlite3')
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    records = cursor.fetchall()
    return records
