#!/usr/bin/python3
'''
Filter states
'''

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        db = MySQLdb.connect(host="localhost",
                             port=3306, user=username,
                             passwd=password, db=database)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM states
                       WHERE name LIKE 'N%' ORDER BY id ASC")
        for row in cursor.fetchall():
            print(row)
            cursor.close()
            db.close()
