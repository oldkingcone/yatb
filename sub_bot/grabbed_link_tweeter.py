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

auth = tweepy.OAuthHandler(consumer_key=consumer_key, consumer_secret=consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth,  wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)
sleep = random.randint(1000,5000)

def random_line(afile):
    seen = set()
    line = next(afile)
    for num, aline in enumerate(afile):
        if random.randrange(num+2): continue
        line = aline
        if line not in seen:
            print("[!] Selecting %s [!]" % str(line))
            seen.add(str(line))
            return line
        if line in seen:
            print("[!!] Already processed that line, skipping. [!!]")
            continue
    return line


def progress_bar(duration):
    for i in tqdm(range(int(duration))):
        time.sleep(1)
while True:
    choice = random.randint(1,3)
    if choice == 1:
        print("[~] Python Selected [~]\n")
        try:
            f_name = open("./links/grabbed_links_python.txt", "r")
            feed = random_line(f_name) + ' ' + "#ilovepythonmore"
            api.update_status(feed)
        except Exception as e:
            print(str(e))
            continue
        progress_bar(sleep)
    if choice == 2:
        print("[~] Infosec selected! [~]\n")
        try:
            f_name = open("./links/grabbed_links_infosec.txt", "r")
            feed = random_line(f_name) + ' ' + "#ilovepythonmore"
            api.update_status(feed)
        except Exception as e:
            print(str(e))
            continue
        progress_bar(sleep)
    if choice == 3:
        print("[~] Linux Selected [~]\n")
        try:
            f_name = open("./links/grabbed_links_shell.txt", "r")
            feed = random_line(f_name) + ' ' + "#ilovepythonmore"
            api.update_status(feed)
        except Exception as e:
            print(str(e))
            continue
        progress_bar(sleep)

