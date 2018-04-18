import tweepy
from time import sleep
from creds import *
from datetime import datetime as dt
import random
from tqdm import tqdm
import time
import sys

def progress_bar(duration):
    for i in tqdm(range(duration)):
        time.sleep(1)

auth = tweepy.OAuthHandler(consumer_key=consumer_key, consumer_secret= consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)
cont = 'true'
while cont == 'true':
    q = ''
    summer = '#summervibe'
    nature = '#naturephotography'
    ocean = '#oceanfront'
    select = random.randint(1,3)
    if select == 1: q=summer
    if select == 2: q = nature
    if select == 3: q = ocean
    print("Choosing: %s" %str(q))
    for tweet in tweepy.Cursor(api.search, q=q).items(5):
        try:
            sleep_time = random.randint(100,1000)
            date = dt.now()
            print("\nTweet by: @"+tweet.user.screen_name)
            print("time stamped: %s" %str(date))
            try:
                tweet.retweet()
                print("Successfully retweeted!")
            except:
                print("Has already been retweeted")
                pass
            try:
                 tweet.favorite()
                 print("Successfully favorited!")
            except:
                print("Has already been favorited")
                pass
            try:
                tweet.user.follow()
                print("Successfully followed user!")
            except:
                print("Already following.")
                pass
                # print("Tweet favorited, and user has been followed!")
            progress_bar(sleep_time)
            sys.stdout.flush()
        except tweepy.TweepError as e:
            print("Something happened: %s"%str(e))
            sleep(5)
            continue
        except StopIteration:
            break
