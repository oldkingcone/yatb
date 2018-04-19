import tweepy
# from time import sleep
import time
from creds import *
import os
from datetime import datetime as dt
import random
from tqdm import tqdm
auth = tweepy.OAuthHandler(consumer_key=consumer_key, consumer_secret=consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth,  wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

def already_tweeted(user):
    finished = list()
    run_through = list()
    listing = tweepy.Cursor(api.followers_ids(user)).items(100)
    print("[**] Validating friendslist, and sending thank yous [**]")
    if user not in finished:
        finished.append(user)
        run_through.append(user)
        print("[**] Its a fresh one! [**]")
        for item in listing:
            if api.show_friendship(api.me(), item) == True:
                tanks = "Thank you for showing love for python like i do :) #ilovepythonmore " + item
                api.update_status(tanks)
    else:
        return True
    return False

def progress_bar(duration):
    for i in tqdm(range(int(duration))):
        time.sleep(1)

cont = 0
yes = 'true'
os.system('clear')
python = '#python'
bash = '#bash'
scripting = '#scripting'
prog = '#programming'
sec = '#infosec'
while yes == 'true':
    if cont == 0:
        # cont = 0
        choice = random.randint(1, 5)
        q = ''
        # print(choice)
        if choice == 1:
            q = python
            print("\nChosing %s for search criteria." % str(q))
            for tweet in tweepy.Cursor(api.search, q=q, locale='en').items(10):
                try:
                    sleep_time = random.randint(10, 550)
                    date_1 = dt.now()
                    print('\nTweet by: @' + tweet.user.screen_name)
                    try:
                        tweet.retweet()
                        print("Retweeted the Found Tweet")
                        print("Time: %s" % str(date_1))
                    except tweepy.TweepError:
                        pass
                    if not tweet.user.following:
                        tweet.user.follow()
                        print("Followed user!")
                    try:
                        print("Favorited the found tweet!")
                        tweet.favorite()
                    except:
                        pass
                    print("Sleep for: %i seconds" % sleep_time)
                    # sleep(sleep_time)
                    progress_bar(sleep_time)
                    # already_tweeted(api.me())
                    cont = 0
                except (tweepy.TweepError) as e:
                    sleep_time = random.randint(10, 50)
                    print("Something happened: %s" % str(e))
                    progress_bar(sleep_time)
                    cont = 0
                    continue
                except StopIteration:
                    break
        if choice == 2:
            q = bash
            print("\nChosing %s for search criteria." % str(q))
            for tweet in tweepy.Cursor(api.search, q=q, locale = 'en').items(10):
                try:
                    sleep_time = random.randint(10, 550)
                    date_1 = dt.now()
                    print('\nTweet by: @' + tweet.user.screen_name)
                    try:
                        tweet.retweet()
                        print("Retweeted the Found Tweet")
                        print("Time: %s" % str(date_1))
                    except tweepy.TweepError:
                        pass
                    if not tweet.user.following:
                        tweet.user.follow()
                        print("Followed user!")
                    try:
                        print("Favorited the found tweet!")
                        tweet.favorite()
                    except tweepy.TweepError:
                        pass
                    print("Sleep for: %i seconds" % sleep_time)
                    progress_bar(sleep_time)
                    cont = 0
                    # continue
                except (tweepy.TweepError) as e:
                    sleep_time = random.randint(10, 50)
                    print("Something happened: %s" % str(e))
                    progress_bar(sleep_time)
                    cont = 0
                    continue
                except StopIteration:
                    break
        if choice == 3:
            q = scripting
            print("\nChosing %s for search criteria." % str(q))
            for tweet in tweepy.Cursor(api.search, q=q, locale='en').items(10):
                try:
                    sleep_time = random.randint(10, 550)
                    date_1 = dt.now()
                    print('\nTweet by: @' + tweet.user.screen_name)
                    try:
                        tweet.retweet()
                        print("Retweeted the Found Tweet")
                        print("Time: %s" % str(date_1))
                    except tweepy.TweepError:
                        pass
                    if not tweet.user.following:
                        tweet.user.follow()
                        print("Followed user!")
                    try:
                        print("Favorited the found tweet!")
                        tweet.favorite()
                    except tweepy.TweepError:
                        pass
                    print("Sleep for: %i seconds" % sleep_time)
                    progress_bar(sleep_time)
                    cont = 0
                    # continue
                except (tweepy.TweepError) as e:
                    sleep_time = random.randint(10, 50)
                    print("Something Happened: %s" % str(e))
                    progress_bar(sleep_time)
                    cont = 0
                    continue
                except StopIteration:
                    break
        if choice == 4:
            q = prog
            print("\nChosing %s for search criteria." % str(q))
            for tweet in tweepy.Cursor(api.search, q=q, locale='en').items(10):
                try:
                    sleep_time = random.randint(10, 550)
                    date_1 = dt.now()
                    print('\nTweet by: @' + tweet.user.screen_name)
                    try:
                        tweet.retweet()
                        print("Retweeted the Found Tweet")
                        print("Time: %s" % str(date_1))
                    except tweepy.TweepError:
                        pass
                    if not tweet.user.following:
                        tweet.user.follow()
                        print("Followed user!")
                    try:
                        print("Favorited the found tweet!")
                        tweet.favorite()
                    except tweepy.TweepError:
                        pass
                    print("Sleep for: %i seconds" % sleep_time)
                    progress_bar(sleep_time)
                    cont = 0
                    # continue
                except (tweepy.TweepError) as e:
                    sleep_time = random.randint(10, 50)
                    print("Something happened: %s" % str(e))
                    progress_bar(sleep_time)
                    cont = 0
                    continue
                except StopIteration:
                    break
        if choice == 5:
            q = sec
            print("\nChosing %s for search criteria." % str(q))
            for tweet in tweepy.Cursor(api.search, q=q).items(10):
                try:
                    sleep_time = random.randint(10, 550)
                    date_1 = dt.now()
                    print('\nTweet by: @' + tweet.user.screen_name)
                    try:
                        tweet.retweet()
                        print("Retweeted the Found Tweet")
                        print("Time: %s" % str(date_1))
                    except tweepy.TweepError:
                        pass
                    if not tweet.user.following:
                        tweet.user.follow()
                        print("Followed user!")
                    try:
                        print("Favorited the found tweet!")
                        tweet.favorite()
                    except:
                        pass
                    print("Sleep for: %i seconds" % sleep_time)
                    progress_bar(sleep_time)
                    cont = 0
                    # continue
                except (tweepy.TweepError) as e:
                    sleep_time = random.randint(10, 50)
                    print("Something Happened: %s" % str(e))
                    progress_bar(sleep_time)
                    cont = 0
                    continue
                except StopIteration:
                    break
