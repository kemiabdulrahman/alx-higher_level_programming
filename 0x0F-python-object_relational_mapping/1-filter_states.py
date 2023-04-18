#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    dt = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], dt=sys.argv[3], port=3306)
    cur = dt.cursor()
    cur.execute("""SELECT * FROM states WHERE name
                 LIKE BINARY 'N%' ORDER BY states.id""")
    rows = cur.fetchall()
    for i in rows:
        print(i)
    cur.close()
    dt.close()
