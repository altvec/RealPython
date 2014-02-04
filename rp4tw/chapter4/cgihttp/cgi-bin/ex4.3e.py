#!/usr/bin/env python

import cgi

form = cgi.FieldStorage()

user = cgi.escape(form['user'].value) if 'user' in form else ''
passwd = cgi.escape(form['password'].value) if 'password' in form else ''

username = "admin"
password = "admin"

if (user == username and password == password):
    msg = "Welcome {username}. You're now logged in.".format(username=username)
else:
    msg = "Incorrect username or password. Please try again."

print "Content-type: text/html\n"
htmlFormat = """
<html>
    <body>
        <p>{msg}</p>
    </body>
</html>
"""
print htmlFormat.format(msg=msg)
