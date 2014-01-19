import sqlite3

with sqlite3.connect("cars.db") as connection:
    '''
    Table: inventory
    Fields: make (TEXT), model (TEXT), quantity (INT)
    '''
    c = connection.cursor()
    c.execute("SELECT model, quantity FROM inventory WHERE make='Ford'")
    rows = c.fetchall()
    for row in rows:
        print row
