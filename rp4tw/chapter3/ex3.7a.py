import sqlite3
import json
import os
import requests

home_dir = os.getenv("HOME")

settings = json.load(open
    (os.path.join(home_dir, "Dropbox/Private/tomatoes.json")))

api_key = settings["key"]

url = requests.get("http://api.rottentomatoes.com/api/public/v1.0/lists/movies/in_theaters.json?apikey=%s" % (api_key,))

# convert data from feed to binary
binary = url.content

# decode json feed
output = json.loads(binary)

# grab the list of movies
movies = output["movies"]

with sqlite3.connect("movies.db") as connection:
    c = connection.cursor()

    c.execute("DROP TABLE IF EXISTS new_movies")
    c.execute("""CREATE TABLE new_movies
              (title TEXT, year INT, rating TEXT,
              release TEXT, runtime INT, critics_review INT,
              audience_review INT)""")
    # write data to DB
    for movie in movies:
        c.execute("INSERT INTO new_movies VALUES(?,?,?,?,?,?,?)",
                  (movie["title"], movie["year"], movie["mpaa_rating"],
                   movie["release_dates"]["theater"], movie["runtime"],
                   movie["ratings"]["critics_score"],
                   movie["ratings"]["audience_score"]))

    # retrieve data
    c.execute("SELECT * FROM new_movies ORDER BY title ASC")

    rows = c.fetchall()

    for r in rows:
        print r[0], r[1], r[2], r[3], r[4], r[5], r[6]
