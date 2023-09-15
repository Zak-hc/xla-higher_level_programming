#!/usr/bin/python3
"""listing all states with starting with N from the db"""
import MySQLdb
import sys


def printcondi():

    n = MySQLdb.connect(host='localhost',
                        user=sys.argv[1],
                        passwd=sys.argv[2],
                        db=sys.argv[3],
                        port=3306)
    v = n.cursor()
    v.execute(
            "SELECT * FROM states WHERE BINARY name lIKE 'N%' ORDER BY id ASC")
    i = v.fetchall()
    for y in i:
        print(y)
    n.close()


if __name__ == "__main__":
    printcondi()
