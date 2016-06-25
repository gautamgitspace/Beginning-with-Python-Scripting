import urllib
import xml.etree.ElementTree as ET
l=list()
totalSum = 0
pageHandle = urllib.urlopen('http://python-data.dr-chuck.net/comments_279922.xml')
data = pageHandle.read()
#print data
tree = ET.fromstring(data)
l = tree.findall('comments/comment')
print 'Total User Count:', len(l)
print 'Beginning parsing. . .\n'
for item in l:
    print 'Name:', item.find('name').text
    print 'Count:', item.find('count').text
    totalSum = totalSum + float(item.find('count').text)
print ('\nCalculating sum count. . .\n')
print totalSum