import sqlite3

# importing config variable from configuration file 'config.py'
from config import DATABASE_PATH

with sqlite3.connect(DATABASE_PATH) as connection:
    c = connection.cursor()
    c.execute("""
        CREATE TABLE tasks(task_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            due_date TEXT NOT NULL,
            priority INTEGER NOT NULL,
            status INTEGER NOT NULL)""")

    # insert dummy data
    c.execute('INSERT INTO tasks (name, due_date, priority, status) \
        VALUES("Finish this tutorial", "02/03/2013", 10, 1)')
    c.execute('INSERT INTO tasks (name, due_date, priority, status) \
        VALUES("Finish this book", "02/03/2013", 10, 1)')
