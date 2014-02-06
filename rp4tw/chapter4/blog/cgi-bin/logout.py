#!/usr/bin/env python

""" Logout """
import Cookie

thiscookie = Cookie.SimpleCookie()
thiscookie['logged_in'] = ''
print thiscookie

# redirect to login page
print "Refresh: 0; url=../login.html\r\n"
