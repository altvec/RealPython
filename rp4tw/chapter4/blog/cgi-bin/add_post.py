#!/usr/bin/env python

""" Add post """

import sqlite3
import cgi
import os
import time
import Cookie

logged_in = False

# check if the user is authenticated through a cookie
thiscookie = Cookie.SimpleCookie()
if os.environ.has_key('HTTP_COOKIE'):
    thiscookie.load(os.environ['HTTP_COOKIE'])
    if 'logged_in' in thiscookie:
        logged_in = bool(thiscookie['logged_in'].value)

# redirect to login page if not authenticated
if not logged_in:
    print "Refresh: 0; url=../login.html\r\n"

print "Content-Type: text/html\n"

form = cgi.FieldStorage()

title = form.getfirst('title', '')
post = form.getfirst('post', '')

with sqlite3.connect("blog_database.db") as connection:
    c = connection.cursor()

    if (title != "" and post != ""):
        date = time.strftime("%x")
        c.execute("INSERT INTO posts VALUES(?,?,?)", (date, title, post))

    c.execute("SELECT COUNT(post) FROM posts")
    total = c.fetchone()[0]

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
            <div>
                <form method="POST" action="add_post.py">
                    <h2>Add new post:</h2>
                    <p>Title:
                        <input type="text" name="title" value="">
                    </p>
                    <p>Post:
                        <input type="text" name="post" value="">
                    </p>
                    <input type="submit" value="Submit">
                </form>
            </div>
        </body>
    </html>
    """ % (total, data_table)
