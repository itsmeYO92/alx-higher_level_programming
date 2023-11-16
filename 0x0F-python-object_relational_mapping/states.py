#!/usr/bin/python3

import MySQLdb
import sys


db = MySQLdb.connect(user = sys.argv[1], password = sys.argv[2], database = sys.argv[3] )

cursor = db.cursor()

cursor.execute("SELECT * FROM states WHERE name = %s", sys.argv[4])
states = cursor.fetchall()
for state in states:
    print(state)
cursor.close()
db.close()
