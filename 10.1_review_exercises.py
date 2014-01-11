'''
Task description:
=================

- Write script that grabs the full HTML from the page dionysus.html
(http://www.realpython.com/practice/dionysus.html)
- Using the string find() method to display the text following "Name:"
and "Favorite Color:" (not including any leading spaces or trailing HTML
tags might apper on the same line)
- Repeat the previous exercise using regular expressions; the end of each
pattern should be a "<" (i.e., the start of an HTML tag) or a newline
character, and you should remove any extra spaces of newline characters
from the resulting text
'''

import re
from urllib2 import urlopen

addr = "http://realpython.com/practice/dionysus.html"
page = urlopen(addr)
text = page.read()

# using strings find() merthod
for w in ["Name: ", "Favorite Color: "]:
    w_start = text.find(w) + len(w)
    w_end = text[w_start:].find("<")
    print text[w_start:w_start+w_end].strip("\n")

# using re
for w in ["Name: .*?[\n<]", "Favorite Color: .*?[\n<]"]:
    matchResults = re.search(w, text)
    result = re.sub(".*: ", "", matchResults.group())
    print result.strip(" \n<")
