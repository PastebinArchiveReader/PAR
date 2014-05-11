"""
    Python Archive Reader 1.0
    https://github.com/PastebinArchiveReader/PAR

"""

import requests
from bs4 import BeautifulSoup
import urllib
import argparse
import time

# add parsing functionality to provide files
parser = argparse.ArgumentParser(description="Script to download pastebin archives",
                                 epilog='''You can download different archives from pastebin.com with this script.
                                 Simply specify a language and extension you wish to download.''')
parser.add_argument("-l", "--language", dest="language", help="specify specify the language",
                    metavar="python, csharp, cpp, etc.")
parser.add_argument("-e", "--extension", dest="extension", help="file extension of the language",
                    metavar="extension")
parser.add_argument("-p", "--path", dest="path", help="where to save the downloaded files",
                    metavar="/home/anon/scripts")
args = parser.parse_args()

url = "http://pastebin.com/archive/" + args.language

while 1:

    source = requests.get(url)
    soup = BeautifulSoup(source.text)

    for link in soup.find_all('a'):
        if len(link.get('href')) == 9:
            if link.get(
                    'href') != "/settings":  # "/settings" is just a 9-characters configuration file from Pastebin.com. Pointless.
                ID = link.get('href')
                paste = link.get('href').replace('/', '')
                paste = "http://www.pastebin.com/raw.php?i=" + paste
                print("[?] {}".format(paste))

                downloaded_file = args.path + "/" + ID + args.extension
                urllib.urlretrieve(paste, downloaded_file)
                print("[!] Downloaded !\n")
                time.sleep(3.5)  # If the delay is smaller, Pastebin.com will block your IP

    print("Finished !")
    time.sleep(1)
    print("Restarting...")
