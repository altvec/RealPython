#!/usr/bin/env python

""" Create DATABASE """

import sqlite3

# create a new database
with sqlite3.connect("blog_database.db") as connection:
    c = connection.cursor()
    c.execute("""CREATE TABLE posts(date_time TEXT, title TEXT, post TEXT)""")

    # sample posts
    posts = [
        ("01.01.1970", "Good", "I\'m good."),
        ("02.01.1970", "Well", "I\'m well.")
    ]

    c.executemany('INSERT INTO posts VALUES(?,?,?)', posts)
