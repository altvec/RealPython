import sqlite3

with sqlite3.connect("cars.db") as connection:
    '''
    Table: inventory
    Fields: make (TEXT), model (TEXT), quantity (INT)
    '''
    c = connection.cursor()
    cars = [
        ('Ford', 'T', 5),
        ('Ford', 'Fiesta', 100),
        ('Ford', 'Mustang', 2),
        ('Honda', 'Prelude', 5),
        ('Honda', 'Accord', 15)
    ]
    c.executemany('INSERT INTO inventory VALUES(?, ?, ?)', cars)
