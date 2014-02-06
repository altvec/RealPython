#!/usr/bin/env python

""" Login """

import cgi
import Cookie

form = cgi.FieldStorage()

post_user = form.getfirst('user', '')
post_password = form.getfirst('password', '')

# our username and password
username = "admin"
password = "admin"

if (post_user == username and post_password == password):
    thiscookie = Cookie.SimpleCookie()
    thiscookie['logged_in'] = True
    print thiscookie
    print "Refresh: 0; url=main.py\r\n"
else:
    print "Refresh: 0; url=../login.html\r\n"
