import tweepy
import os
import json

home_dir = os.getenv("HOME")

settings = json.load(open
    (os.path.join(home_dir, "Dropbox/Private/twitter_api.json")))

consumer_key = settings["consumer_key"]
consumer_secret = settings["consumer_secret"]
access_token = settings["access_token"]
access_secret = settings["access_secret"]

auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

tweets = api.search(q='Kiev')

for tw in tweets:
    print tw.created_at, tw.text, "\n"
