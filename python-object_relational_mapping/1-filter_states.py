#!/usr/bin/python3
"""Task 1"""


import sys
import MySQLdb

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username, passwd=mysql_password, db=database_name)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id")
    states = cursor.fetchall()
    for state in states:
        if state[1][0] == "N":
            print(state)
    cursor.close()
    db.close()
