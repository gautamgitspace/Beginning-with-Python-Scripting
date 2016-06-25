import json
import urllib
url = raw_input('Enter location: ')
print 'Retrieving', url
urlHandle = urllib.urlopen(url)
data = urlHandle.read()
length = len(data)
print 'Retrieved ' + str(length) + ' characters'
jsdata = json.loads(data)
#print json.dumps(jsdata, indent=4)
#print len(jsdata["comments"])
i=0
sum = 0
while i < 50:
    sum = sum + jsdata["comments"][i]["count"]
    i = i+1
print sum