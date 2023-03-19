#!/usr/bin/python3
""" Task 0 """


if __name__ == "__main__":

    import MySQLdb
    import sys

    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()

    query = "SELECT * FROM states WHERE name LIKE BINARY %s"

    name = (sys.argv[4],)

    cur.execute(query, name)

    rows = cur.fetchall()

    for row in rows:
        print(row)
