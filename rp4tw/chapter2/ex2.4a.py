import sqlite3

with sqlite3.connect("employees.db") as connection:
    c = connection.cursor()

    for row in c.execute("SELECT firstname, lastname FROM employees"):
        print row
