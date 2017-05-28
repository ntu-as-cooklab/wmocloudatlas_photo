from json import load
from os import makedirs, getcwd, path
from bs4 import BeautifulSoup
import requests
import codecs
import sys
import urllib

# I/O encoding, see https://stackoverflow.com/questions/14630288
if sys.stdout.encoding != 'cp850':
    sys.stdout = codecs.getwriter('cp850')(sys.stdout, 'strict')
if sys.stderr.encoding != 'cp850':
    sys.stderr = codecs.getwriter('cp850')(sys.stderr, 'strict')

HOME_LINK = "https://www.wmocloudatlas.org"

with open('pageLink.json') as data_file:
    print ("Loading json..")
    pageLink = load(data_file)

for cloudType in pageLink:
    dic_path = getcwd() + "/photo/" + cloudType
    if not path.isdir(dic_path):
        makedirs(dic_path)
    for link in pageLink[cloudType]:
        try:
            print("Dealing " + link)
            doc = requests.get(link).text
            soup = BeautifulSoup(doc)
            imgLink = soup.find('img', id='img1')
            photoLink = HOME_LINK + imgLink["src"].split(".", 1)[1]
            urllib.urlretrieve(photoLink, dic_path + "/" +
                               photoLink.split("compressed/")[1])
        except Exception:
            print("Error at link: " + link)
