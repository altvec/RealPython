'''
Task description:
=================
- Write a script that grabs the full HTML from the page
http://www.realpython.com/practice/profiles.html
- Parse out a list of all the links on the page using Beautiful Soup by
looking for HTML tags with the name "a" and retrieving the value taken on
by the "href" attribute of each tag
- Get the HTML from each of the pages in the list by adding the full path
to the file name, and display the text (without HTML tags) on each page
using Beautiful Soup's get_text() method
'''
