import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()
    c.execute("CREATE TABLE orders(make TEXT, model TEXT, order_date DATE)")

    orders = [
        ('Ford', 'T', '2014-01-01'),
        ('Ford', 'Fiesta', '2014-01-02'),
        ('Ford', 'Mustang', '2014-01-03'),
        ('Honda', 'Prelude', '2014-01-04'),
        ('Honda', 'Accord', '2014-01-05'),
        ('Ford', 'T', '2014-01-06'),
        ('Ford', 'Fiesta', '2014-01-07'),
        ('Ford', 'Mustang', '2014-01-08'),
        ('Honda', 'Prelude', '2014-01-09'),
        ('Honda', 'Accord', '2014-01-10'),
        ('Ford', 'T', '2014-01-11'),
        ('Ford', 'Fiesta', '2014-01-12'),
        ('Ford', 'Mustang', '2014-01-13'),
        ('Honda', 'Prelude', '2014-01-14'),
        ('Honda', 'Accord', '2014-01-15')
    ]

    c.executemany("INSERT INTO orders VALUES(?,?,?)", orders)
    c.execute("SELECT * FROM inventory")
    rows = c.fetchall()
    for i in rows:
        print i[0], i[1]
        print i[2]
        c.execute("SELECT order_date FROM orders WHERE make=? AND model=?",
                  (i[0], i[1]))
        order_dates = c.fetchall()
        for d in order_dates:
            print d[0]
