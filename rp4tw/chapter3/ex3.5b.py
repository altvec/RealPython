import json

output = json.load(open('cars.json'))

'''
[0]["CAR"] - we want to find the first car dictionary. Since the is
only one, there can be only one value - 0.

[0]["MODEL"] - we want to find te first instance of the model key and
then extract the value associated with that key.
'''

print output[0]["CAR"][1]["MODEL"]
