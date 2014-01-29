'''
Task description:
=================
Using the Google Direction API, pull driving directions from San Francisco
to Los Angeles in XML. Extract the step-by-step driving directions.
'''

import requests
import re
from xml.etree import ElementTree as et

url = 'http://maps.googleapis.com/maps/api/directions/xml?origin=San+Francisco&destination=Los+Angeles&sensor=false&mode=driving'

page = requests.get(url)

with open('data.xml', 'wb') as data:
    data.write(page.content)

doc = et.parse('data.xml')

for e in doc.findall("route/leg/step"):
    # do not print <b></b> tags
    print re.sub(r'<.+?>', '', e.find("html_instructions").text)
