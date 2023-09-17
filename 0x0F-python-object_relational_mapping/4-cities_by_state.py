#!/usr/bin/python3
"""
List all cities from the database.

"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    cur = db.cursor()
    query = "SELECT cities.id, cities.name, states.name \
            FROM cities \
            INNER JOIN states ON states.id = cities.state_id"

    cur.execute(query)
    for record in cur.fetchall():
        print(record)

    cur.close()
    db.close()
