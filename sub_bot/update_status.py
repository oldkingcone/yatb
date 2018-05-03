try:
    import tweepy
    import time
    from tqdm import tqdm
    import os
    import sys
    import random
    from creds import *
except ImportError as e:
    print("[**] Something went wrong, sorry: %s [**]" %str(e))
    sys.exit(1)
os.system('clear')
auth = tweepy.OAuthHandler(consumer_key=consumer_key, consumer_secret=consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth,  wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)
loop = True
while loop == True:

    try:
        status = input("[~] What would you like to update your status with? [~]\n->")
        if status == '':
            print("[!] Sorry, cannot put blank updates.... thats rude. [!]")
            continue
        real = status + ' #ilovepythonmore #human #programming #linux'
        api.update_status(status=real)
        os.system('clear')
        print("[!] Update Successful! [!]\n%s" % str(real))
    except KeyboardInterrupt:
        print("[!] Good-bye [!]")
        loop = False
