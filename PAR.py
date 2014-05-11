"""
	Python Archive Reader 1.0
	https://github.com/PastebinArchiveReader/PAR

"""

import requests
from bs4 import BeautifulSoup
import urllib
import sys
import time

language = sys.argv[1] #python, csharp, cpp, haskell...
extension = sys.argv[2] #.py, .cs, .cpp, .hs...
path = sys.argv[3] #the folder where files will be downloaded, like /home/anon/scripts/

url = "http://pastebin.com/archive/" + language

while 1:

	source = requests.get(url)
	soup = BeautifulSoup(source.text)

	for link in soup.find_all('a'):
		if len(link.get('href')) == 9:
			if link.get('href') != "/settings": #"/settings" is just a 9-characters configuration file from Pastebin.com. Pointless.
				ID = link.get('href')
				paste = link.get('href').replace('/', '')
				paste = "http://www.pastebin.com/raw.php?i=" + paste
				print("[?] {}".format(paste))

				downloaded_file = path + "/" + ID + extension
				urllib.urlretrieve(paste, downloaded_file)
				print("[!] Downloaded !\n")
				time.sleep(3.5) #If the delay is smaller, Pastebin.com will block your IP

	print("Finished !")
	time.sleep(1)
	print("Restarting...")
