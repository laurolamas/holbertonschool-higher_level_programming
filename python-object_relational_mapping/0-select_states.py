#!/usr/bin/python3
""" Task 0 """


if __name__ == "__main__":

    import MySQLdb
    import sys

    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()

    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()
    for row in rows:
        print(row)