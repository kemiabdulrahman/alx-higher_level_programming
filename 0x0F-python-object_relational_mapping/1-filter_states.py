#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == "__main__":
    database = MySQLdb.connect(host = "localhost", username=sys.argv[1], password = sys.argv[2], database=sys.argv[3], port=3306)
    cursor = database.cursor()
    cursor.execute("""SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY states.id""")
    rows = cursor.fetchall()
    for i in rows:
        print(i)
    cursor.close()
    database.close()
