import requests
import time

i = 0
while (i < 2):
    base_url = "http://download.finance.yahoo.com/d/quotes.csv"
    data = requests.get(base_url,
                        params={'s': 'GOOG', 'f': 'sl1d1t1c1ohgv',
                                'e': '.csv'})

    # write data to csv
    with open("stocks.csv", "a") as output:
        output.write(data.content)
    i += 1

    # pause for 3 sec
    time.sleep(3)
