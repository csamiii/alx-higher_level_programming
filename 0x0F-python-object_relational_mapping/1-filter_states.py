#!/usr/bin/python3

""" List all states starting with N """

import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(
        host="localhost", usr=agrv[1], passwd=argv[2], db=argv[3], port=3306)
    db_cur = db.cursor()
    db_cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id")
    n_rows = db_cur.fetchall()
    for n in n_rows:
        print(n)
    db_cur.close()
    db.close()
