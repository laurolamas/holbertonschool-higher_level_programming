#!/usr/bin/python3
""" Task 0 """


if __name__ == "__main__":

    import MySQLdb
    import sys

    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()

    query = "SELECT cities.name FROM cities JOIN states \
        ON cities.state_id = states.id WHERE states.name LIKE %s"

    name = (sys.argv[4],)

    cur.execute(query, name)

    rows = cur.fetchall()

    output = ""
    for row in rows:
        output += f"{row[0]}, "
    print(output[:-2])
