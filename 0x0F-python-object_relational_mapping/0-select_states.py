#!/usr/bin/python3
import MySQLdb
import sys

# Connect to a MySQL database and return the connection and cursor objects.
if __name__ == "__main__":

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    sync = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name)
    cursor = sync.cursor()

# Query to select all states from the in ascending order.
    sql_coo = "SELECT * FROM states ORDER BY id ASC"
    cursor.execute(sql_coo)

# Fetch all the results.
    lines = cursor.fetchall()

# Display the results.
    for line in lines:
        print(line)

# Close the database connection.
    sync.close()
