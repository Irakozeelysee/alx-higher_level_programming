#!/usr/bin/python3
"""
list all states from db.
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3])
    cur = db.cursor()
    query = "SELECT * FROM states ORDER BY states.id ASC"
    cur.execute(query)

    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
