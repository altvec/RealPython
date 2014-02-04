#!/usr/bin/env python
import cgi
form = cgi.FieldStorage()

# retrieve the name from the form, set the empty string if none
name = cgi.escape(form['name'].value) if 'name' in form else ''
print "Content-Type: text/html\n"
htmlFormat = """
<html>
    <body>
        <p>Hi, {name}</p>
    </body>
</html>
"""
print htmlFormat.format(name=name)
