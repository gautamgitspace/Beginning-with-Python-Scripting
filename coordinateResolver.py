import urllib
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = raw_input('\nEnter the location: ')
    if len(address) < 1:
        print 'Please verify your address'
        break
    url = serviceurl + urllib.urlencode({'sensor': 'false', 'address': address})
    print 'NEW URL:', url
    urlHandle = urllib.urlopen(url)
    data = urlHandle.read()
    length = len(data)
    print 'RECEIVED BYTES OF DATA:', length
    try:
        jsdata = json.loads(data)
    except:
        jsdata = None
    if 'status' not in jsdata or jsdata['status']!='OK':
        print 'could not retrieve'
    else:
        print jsdata
        continue


