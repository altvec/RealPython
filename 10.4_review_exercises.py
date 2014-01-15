'''
Task description:
=================
Repeat the example in this section to scrape YHOO stock quotes, but
additionaly include the current time of the quote as obtained from the
Yahoo! Finance webpage; this time can be taken from part of a string inside
another span tag that appears shortly after the actual stock price in the
webpage's HTML
'''

from time import sleep
from bs4 import BeautifulSoup
import mechanize

browser = mechanize.Browser()

for i in range(0, 5):
    page = browser.open("http://finance.yahoo.com/q?s=yhoo")
    text = page.get_data()
    soup = BeautifulSoup(text)
    priceTag = soup.find_all("span", id="yfs_l84_yhoo")
    _price = priceTag[0].string
    timeTag = soup.find_all("span", id="yfs_t53_yhoo")
    _time = timeTag[0].string

    print "At {} the current price of YHOO is: {}".format(_time, _price)
    if i < 2:
        sleep(60)
