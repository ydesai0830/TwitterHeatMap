#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import json
import pandas as pd
import matplotlib.pyplot as plt

#Variables that contains the user credentials to access Twitter API 
access_token = "137875398-pt9IRGEUovXJsPX9qUR6GnN3v6wfGxJ5FXjNB8ni"
access_token_secret = "g98Rzyz8ikbdckeeNhTcEK7hvWo4VylobX3mbfPzRBHzo"
consumer_key = "YyzWFm2M80BSUivIvIDj9cJf9"
consumer_secret = "t9UuGFbYTynF11E4FSD6wkr0IWUeKCbzLOu1y1TR4XZhyt5UHC"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)

def streamTweets():
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])

def aggregateTweets():
    tweets_data_path = 'twitter_data.txt'

    tweets_data = []
    tweets_file = open(tweets_data_path, "r")
    for line in tweets_file:
        try:
            tweet = json.loads(line)
            tweets_data.append(tweet)
        except:
            continue

    return tweets_data

def setUpDataFrame(tweets_data):
    tweets = pd.DataFrame()
    tweets['text'] = tweets_data['text']
    tweets['lang'] = tweets_data['country']
    tweets['country'] = tweet['place']['country'] if tweet['place'] != None else None
    return tweets

if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    tweets_data = aggregateTweets()
    tweets = setUpDataFrame(tweets_data)
    print(tweets)
    



