# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 19:31:06 2017

@author: MANSI
"""

import sys
import pymongo
import tweepy
-
from tweepy import OAuthHandler, Stream, API
from tweepy.streaming import StreamListener

client = pymongo.MongoClient('localhost', 27017)
db = client.test

consumer_key="BgmgtBNn09WKIeXzOQM0xOg8e"
consumer_secret="mYex9vfLZmFyuwEMgJf4XaVb9rMIj4dDqC1W5M5wcX59XQZu6M"

access_token="853536519738597376-X8v0W9bgWmMvDedrwbOMdOQnvhFaPBJ"
access_token_secret="woSLRxB0qPra1qPkMSuQiwn7Oy8zztpK75uJ7DvaZAViB"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = API(auth)

class CustomListener(StreamListener):
  def __init__(self, api):
    self.api = api
    super(tweepy.StreamListener, self).__init__()
    self.db = pymongo.MongoClient().iplt20

  def on_status(self, tweet):
    data = {}
    data['text'] = tweet.text
    data['user'] = tweet.user.screen_name
    data['created_at'] = tweet.created_at
    data['geo'] = tweet.geo
    
    print data, '\n'
    self.db.Tweets.insert_many(data)

  def on_error(self, status):
    print >> sys.stderr, 'Error: ', status
    return True

  def on_timeout(self):
    print >> sys.stderr, 'Stream timeout'
    return True

listen = Stream(auth, CustomListener(api))
listen.filter(track=['iplt20','Fantasyiplt20'])
