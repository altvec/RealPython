import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    # dictionary of SQL queries
    sql = {
        'average': "SELECT avg(population) FROM population",
        'maximum': "SELECT max(population) FROM population",
        'minimum': "SELECT min(population) FROM population",
        'sum': "SELECT sum(population) FROM population",
        'count': "SELECT count(population) FROM population"
    }

    # for each SQL query item in the dictionary
    for keys, values in sql.iteritems():
        c.execute(values)
        # retrieve one record from the query
        result = c.fetchone()
        print keys + ":", result[0]
