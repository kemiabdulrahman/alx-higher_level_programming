#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == '__main__':
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    conn = MySQLdb.connect(
        host='localhost',
        user=mysql_username,
        passwd=mysql_password,
        db=database_name,
        port=3306
    )
    cur = conn.cursor()
    cur.execute('SELECT * FROM states ORDER BY id ASC')
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
