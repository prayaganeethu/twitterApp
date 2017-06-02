try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser  # ver. < 3.0
import tweepy
from flask import render_template, flash, redirect, Flask
from tweepy import OAuthHandler
import json
from tweepy.parsers import JSONParser
import re

app = Flask(__name__)

config = ConfigParser()

config.read('keys.ini')

consumer_key = config.get('twitter', 'consumer_key')
consumer_secret = config.get('twitter', 'consumer_secret')
access_token = config.get('twitter', 'access_token')
access_secret = config.get('twitter', 'access_secret')

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

# api = tweepy.API(auth, parser=JSONParser())

api = tweepy.API(auth)

# text = []
# url = []
# count = 0

statuses = tweepy.Cursor(api.home_timeline).items(20)
# text[count] = status.text
# urls = re.findall(
#     'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', status.text)
# url[count] = urls
# count += 1

# statuses = api.search(id="TechCrunch")
# json_str = json.dumps(statuses)
# for status in tweepy.Cursor(api.home_timeline).items(20):
#     print(status)


@app.route('/')
def tweets():
    return render_template("tweets.html", statuses=statuses)

app.run(debug=True)
