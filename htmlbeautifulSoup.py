import urllib
from bs4 import BeautifulSoup

soup = BeautifulSoup(urllib.urlopen('http://python-data.dr-chuck.net/comments_279925.html').read())

# List of <a> tags
tags = soup('span')

total = 0
for tag in tags:
    total += int(tag.contents[0])

print 'Sum ', total