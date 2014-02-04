#!/usr/bin/env python
import cgi, math

form = cgi.FieldStorage()

value = cgi.escape(form['sqrt'].value) if 'sqrt' in form else 0
sqrt = str(math.sqrt(float(value)))

print "Content-Type: text/html\n"
htmlFormat = """
<html>
    <body>
        <p>Hi. The square root of {value} equals {sqrt}</p>
    </body>
</html>
"""

print htmlFormat.format(value=value, sqrt=sqrt)
