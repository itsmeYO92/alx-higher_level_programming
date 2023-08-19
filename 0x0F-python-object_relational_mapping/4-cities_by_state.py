#!/usr/bin/python3
"""
    select state module that select all stats from a database
"""


import MySQLdb
import sys


def invalid_input(user_input):
    """
        Escapes special charachters to avoid sql injection
    """
    special_chars = ['"', "'", "/", "-", "_", ";", "—"]
    for c in user_input:
        if c in special_chars:
            return True
    return False


if __name__ == '__main__':
    """
        selects the states
    """
    db_args = sys.argv
    db = MySQLdb.connect(
        "localhost", db_args[1], db_args[2], db_args[3], port=3306)

    db_cursor = db.cursor()
    query = "SELECT cities.id, cities.name, states.name FROM cities\
            INNER JOIN states ON cities.state_id = states.id;"
    db_cursor.execute(query)

    results = db_cursor.fetchall()
    for row in results:
        print(row)

    db_cursor.close()
    db.close()
