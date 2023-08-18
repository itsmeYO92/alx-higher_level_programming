#!/usr/bin/python3
"""
    select state module that select all stats from a database
"""


from MySQLdb import _mysql
import sys


if __name__ == '__main__':
    """
        selects the states
    """
    db_args = sys.argv
    db = _mysql.connect("localhost", db_args[1], db_args[2], db_args[3], port=3306)
    
    db.query("""SELECT * FROM states;""")
    
    results = db.store_result()
    rows = results.fetch_row(maxrows=0)
    decoded_rows = [(row[0].decode(), row[1].decode()) for row in rows]
    for row in decoded_rows:
        print(row)
    
    db.close()
