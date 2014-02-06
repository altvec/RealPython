#!/usr/bin/env python

""" Main script """

import sqlite3
import cgi
import os

print "Content-Type: text/html\n"

with sqlite3.connect("blog_database.db") as connection:
    c = connection.cursor()

    # get total posts
    c.execute("SELECT COUNT(post) FROM posts")
    total = c.fetchone()[0]

    # print all posts
    c.execute("SELECT * FROM posts")
    posts = c.fetchall()

    data_table = """
    <table border="1">
        <tr>
            <th>Date</th>
            <th>Title</th>
            <th>Post</th>
        </tr>
    """

    for p in posts:
        data_table += "<tr>"
        data_table += "<td>%s</td>" % (p[0])
        data_table += "<td>%s</td>" % (p[1])
        data_table += "<td>%s</td>" % (p[2])
        data_table += "</tr>"
    data_table += "</table>"

    print """
    <html>
        <head>
            <title>Blog</title>
        </head>
        <body>
            <h1>
                <center>Bloggy</center>
            </h1>
            <h2>Welcome</h2>
            <p>Total Posts: %s</p>
            <p>%s</p>
        </body>
    </html>
    """ % (total, data_table)
