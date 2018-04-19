try:
    from creds import *
    import twitter
    from tqdm import tqdm
    import time
    from random import randint
except (ImportError) as e:
    print("[!!] One of the packages did not import properly %s [!!]" % str(e))

def pyth():
    count = 0
    tweets = stream.statuses.filter(track='python')
    while count != 50:
        for tweet in tweets:
            print("\n(%s) @%s %s" % (tweet["created_at"], tweet["user"]["screen_name"], tweet["text"]))
            for url in tweet["entities"]["urls"]:
                count = count + 1
                with open('./links/grabbed_links_python.txt', 'a') as yes:
                    writing = [str(url["expanded_url"]), '\n']
                    yes.write("".join(writing))
    return False

def shell():
    count = 0
    tweets = stream.statuses.filter(track="shell programming")
    while count != 50:
        for tweet in tweets:
            print("\n(%s) @%s %s" % (tweet["created_at"], tweet["user"]["screen_name"], tweet["text"]))
            for url in tweet["entities"]["urls"]:
                count = count + 1
                with open('./links/grabbed_links_shell.txt', 'a') as yes:
                    writing = [str(url["expanded_url"]), '\n']
                    yes.write("".join(writing))
    return False
def info_sec():
    count = 0
    tweets = stream.statuses.filter(track="infosec")
    while count != 50:
        for tweet in tweets:
            print("\n(%s) @%s %s" % (tweet["created_at"], tweet["user"]["screen_name"], tweet["text"]))
            for url in tweet["entities"]["urls"]:
                count = count + 1
                with open('./links/grabbed_links_infosec.txt', 'a') as yes:
                    writing = [str(url["expanded_url"]), '\n']
                    yes.write("".join(writing))
    return False

def ml():
    count = 0
    tweets = stream.statuses.filter(track="machine learning")
    while count != 10:
        for tweet in tweets:
            print("\n(%s) @%s %s" % (tweet["created_at"], tweet["user"]["screen_name"], tweet["text"]))
            for url in tweet["entities"]["urls"]:
                count = count + 1
                with open('./links/grabbed_links_ml.txt', 'a') as yes:
                    writing = [str(url["expanded_url"]), '\n']
                    yes.write("".join(writing))
    return False
def learning():
    count = 0
    tweets = stream.statuses.filter(track="python ebook")
    while count != 50:
        for tweet in tweets:
            print("\n(%s) @%s %s" % (tweet["created_at"], tweet["user"]["screen_name"], tweet["text"]))
            for url in tweet["entities"]["urls"]:
                count = count + 1
                with open('./links/grabbed_links_ebook.txt', 'a') as yes:
                    writing = [str(url["expanded_url"]), '\n']
                    yes.write("".join(writing))
    return False
restart = "y"
auth = twitter.OAuth(consumer_secret=consumer_secret, consumer_key=consumer_key, token=access_key,
                     token_secret=access_secret)
stream = twitter.TwitterStream(auth=auth, secure=True)
while restart == 'y':
    try:
        selection = ''
        choice = int(input("[**] Please choose:"
                   "\n(1) for Python\n"
                   "(2) for Scripting\n"
                   "(3) Hacking\n"
                   "(4) Machine Learning\n"
                   "(5) Ebooks and the sort [**]"
                   "\n--------------------------\n"
                   "->"))
        if choice == 1:
            print("[!!] Selecting Python! [!!]")
            pyth()
        if choice == 2:
            print("[!!] Selecting Shell Scripting! [!!]")
            shell()
        if choice == 3:
            print("[!!] Selected Hacking! [!!]")
            info_sec()
        if choice == 4:
            print("[!!] Selected Machine Learning [!!]")
            ml()
        if choice == 5:
            print("[!!] Selected Ebooks! [!!]")
            learning()
        continue
    except (KeyboardInterrupt):
        restart = input("[!!] Would you like to restart and re-run? [!!]\n->").lower()