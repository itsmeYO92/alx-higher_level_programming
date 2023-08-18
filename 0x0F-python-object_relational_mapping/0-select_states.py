#!/usr/bin/python3
"""
    select state module that select all stats from a database
"""


import MySQLdb
import sys


if __name__ == '__main__':
    """
        selects the states
    """
    db_args = sys.argv
    db = MySQLdb.connect(
        "localhost", db_args[1], db_args[2], db_args[3], port=3306)

    db_cursor = db.cursor()
    db_cursor.execute("SELECT * FROM states")

    results = db_cursor.fetchall()
    for row in results:
        print(row)

    db_cursor.close()
    db.close()
