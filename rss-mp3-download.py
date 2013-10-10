from BeautifulSoup import NavigableString, BeautifulSoup, BeautifulStoneSoup, Tag
import urllib
import os

INDEX = 'http://5by5.tv/rss'
f = urllib.urlopen(INDEX)
s = f.read()
soup = BeautifulSoup(s)
for item in soup.findAll('item'):
    mp3url = item.find('enclosure').attrs[0][1]
    os.system('wget ' + mp3url)
