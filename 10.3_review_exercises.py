# -*- coding: utf-8 -*-
'''
Task description:
=================

– Use mechanize to provide the correct username "zeus" and password
"ThunderDude" to the login page submission form located at:
http://RealPython.com/practice/login.php
– Using BeautifulSoup, display the title of the current page to determine
that you have been redirected to profiles.html
– Use mechanize to return to login.php by going "back" to the previous
page
– Provide an incorrect username and password to the login form, then
search the HTML of the returned webpage for the text "Wrong username or
password! to determine that the login process failed.
'''

import mechanize
from bs4 import BeautifulSoup

browser = mechanize.Browser()
htmlPage = browser.open("http://realpython.com/practice/login.php")
browser.select_form("login")
browser["user"] = "zeus"
browser["pwd"] = "ThunderDude"
response = browser.submit()
data = response.get_data()
parser = BeautifulSoup(data)
print parser.title.string
print response.geturl()

browser.back()
browser.select_form("login")
browser["user"] = "none"
browser["pwd"] = "lame_pass"
response = browser.submit()
data = response.get_data()

if response.get_data().find("Wrong username or password!") != -1:
    print "Login failed"
else:
    print "Login successful."
