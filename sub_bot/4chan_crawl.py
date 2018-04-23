try:
    import selenium
    import os
    import socket
    from selenium import webdriver
    from selenium.common.exceptions import *
    from time import sleep
    import sys
    from tqdm import tqdm
except ImportError as e:
    print("[!!] One of the selected packages did not import properly %s [!!]" % str(e))
    sys.exit(1)
def progress_bar(duration):
    for i in tqdm(range(int(duration))):
        sleep(1)

driver = webdriver.ChromeOptions()
try:
    driver.add_argument('headless')
    browse = webdriver.Chrome(chrome_options=driver)
except selenium.common.execptions:
    print("[!!] Driver is not in your path, you need to install chromium [!!]")
    sys.exit(1)
loop=1
while loop == 1:
    try:
        os.system('cls')
        try:
            browse.get("https://www.4chan.org")
            print("[**] Pulling data's [**]")
            assert "4chan" in browse.title
        except AssertionError:
            from random import randint
            print("[!] Couldnt get to host... [!]")
            sleep_time = randint(100,500)
            progress_bar(sleep_time)
            continue
        element = browse.find_elements_by_css_selector('#boards > div > div.boxcontent')
        for elem in element:
            with open('./links/grabbed_4chan', 'a') as alf:
                print(str(elem))
                linx = [str(elem), '\n']
                alf.write(''.join(linx))
                alf.close()
    except:
        raise
