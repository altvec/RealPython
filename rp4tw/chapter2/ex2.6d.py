import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    c.execute("""SELECT DISTINCT population.city, population.population,
                 regions.region FROM population, regions
                 WHERE population.city = regions.city
                 ORDER BY population.city ASC""")

    rows = c.fetchall()

    for i in rows:
        print "City: " + i[0]
        print "Population: " + str(i[1])
        print "Region: " + i[2]
        print
