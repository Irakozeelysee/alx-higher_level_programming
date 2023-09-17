#!/usr/bin/python3
"""
List All cities by state
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
    query = "SELECT cities.name \
            FROM cities \
            INNER JOIN states ON states.id = cities.state_id \
            AND states.name = %s"

    cur.execute(query, (argv[4],))
    res = ""
    for record in cur.fetchall():
        if res == "":
            res += record[0]
        else:
            res += ", " + record[0]
    print(res)

    cur.close()
    db.close()
