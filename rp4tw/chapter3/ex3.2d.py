import requests

url = 'http://httpbin.org/post'
data = {'fname': 'Ivan', 'lname': 'Ivanov'}

r = requests.post(url, data=data)

print r.content
