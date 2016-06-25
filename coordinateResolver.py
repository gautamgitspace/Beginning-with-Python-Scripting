import urllib
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
print "I'll try to geo-resolve the location entered by you. type 'DONE' when you're done"
while True:
    try:
        address = raw_input('\nEnter the location: ')
        if address=="done":
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
        #print json.dumps(jsdata, indent=4)
        latitude = jsdata["results"][0]["geometry"]["location"]["lat"]
        longitude = jsdata["results"][0]["geometry"]["location"]["lng"]
        print 'LATITUDE:', latitude
        print 'LONGITUDE:', longitude
        resolvedAddress =  jsdata["results"][0]["formatted_address"]
        print resolvedAddress
        fileHandle = open('output.txt', 'a')
        outputString = str(latitude)+ " " + str(longitude)+ " " + str(resolvedAddress) + "\n"
        fileHandle.write(outputString)
    except:
        print 'INVALID INPUT FOOL'





