#!/usr/bin/env python

import sqlite3
import cgi

print "Content-Type: text/xml\n"

with sqlite3.connect("names.db") as connection:
    c = connection.cursor()

    c.executescript("DROP TABLE IF EXISTS names")
    c.execute("CREATE TABLE names(first TEXT, last TEXT)")

    # fill table with data
    names = [
        ('John', 'Bell'),
        ('Michael', 'Sloane'),
        ('Rachel', 'Peterson')
    ]

    c.executemany('INSERT INTO names VALUES(?,?)', names)
    c.execute("SELECT first, last FROM names")

    # retrieve data
    rows = c.fetchall()

    # build xml string
    print "<names>"
    for r in rows:
        print "\t<name>"
        print "\t\t<first>%s</first>" % (r[0])
        print "\t\t<last>%s</last>" % (r[1])
        print "\t</name>"
    print "</names>"
