#!/usr/bin/env python

""" Create DATABASE """

import sqlite3

# create a new database
with sqlite3.connect("fblog.db") as connection:
    c = connection.cursor()
    c.execute("""CREATE TABLE posts(date_time TEXT, title TEXT, post TEXT)""")

    # sample posts
    posts = [
        ("01/02/12", "Good", "I\'m good."),
        ("02/03/13", "Well", "I\'m well."),
        ("03/04/13", "Okay", "I\'m okay.")
    ]

    c.executemany('INSERT INTO posts VALUES(?,?,?)', posts)
