import sqlite3

with sqlite3.connect("cars.db") as connection:
    '''
    Table: inventory
    Fields: make (TEXT), model (TEXT), quantity (INT)
    '''
    c = connection.cursor()
    c.execute("UPDATE inventory SET quantity=44 WHERE model='T'")
    c.execute("UPDATE inventory SET quantity=1 WHERE model='Prelude'")
    c.execute("SELECT * FROM inventory")
    rows = c.fetchall()
    for row in rows:
        print row
