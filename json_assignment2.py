import json
import urllib
location = raw_input('Enter location: ')
url = 'http://python-data.dr-chuck.net/geojson?'
newUrl = url + urllib.urlencode({'sensor': 'false', 'address': location})
urlHandle = urllib.urlopen(newUrl)
data = urlHandle.read()
jsdata = json.loads(str(data))
#print json.dumps(jsdata, indent=4)
place_id = jsdata["results"][0]['place_id']
print place_id
