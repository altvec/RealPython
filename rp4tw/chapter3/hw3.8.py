import requests
from bs4 import BeautifulSoup

html = requests.get("http://www.web2py.com").text

parse = BeautifulSoup(html)

for link in parse.findAll("a"):
    print link.get("href")
