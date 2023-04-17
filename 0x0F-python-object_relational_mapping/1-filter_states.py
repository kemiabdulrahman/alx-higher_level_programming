#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        username=sys.argv[1],
        password=sys.argv[2],
        db=sys.argv[3],
        port=3306)
    curs = db.cursor()
    curs.execute(
        """SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDE
        R BY states.id""")
    rows = curs.fetchall()
    for i in rows:
        print(i)
    curs.close()
    db.close()
