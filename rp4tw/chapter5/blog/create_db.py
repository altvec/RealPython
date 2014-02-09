#!/usr/bin/env python

""" Create DATABASE """

import sqlite3

# create a new database
with sqlite3.connect("fblog.db") as connection:
    c = connection.cursor()
    c.execute('''CREATE TABLE posts (entry_date DATE CURRENT DATE,
                                     title TEXT,
                                     post TEXT)''')

    # sample posts
    posts = [
        ("Good", "I\'m good."),
        ("Well", "I\'m well."),
        ("Okay", "I\'m okay.")
    ]

    c.executemany('INSERT INTO posts VALUES(date(),?,?)',
                   posts)
