import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("SELECT * FROM inventory")
    rows = c.fetchall()
    for row in rows:
        print "Car's make and model:", row[0], row[1]
        print "Quantity:", row[2]
        c.execute("SELECT COUNT(order_date) FROM orders WHERE make=? AND model=?",
              (row[0], row[1]))

        orders = c.fetchone()[0]
        print "Orders count:", orders
