#parsing XML data in python (DE-SERIALIZE)
import xml.etree.ElementTree as ET

data = '''
<person>
  <name>Vin</name>
  <phone type="intl">
     +1 716 431 9771
   </phone>
   <email hide="yes"/>
</person>'''
#print data
print 'parsing 1st snippet\n'
tree = ET.fromstring(data)
print 'Name:', tree.find('name').text
print 'Phone:', tree.find('phone').text
print 'Attr:', tree.find('email').get('hide')

input = '''
<stuff>
    <users>
        <user x="2">
            <team>Philadelphia</team>
            <name>Allen</name>
            <position>Point Guard</position>
        </user>
        <user x="3">
            <team>Cleveland</team>
            <name>Kyrie</name>
            <position>Point Guard</position>
            </user>
        <user x="4">
            <team>Boston</team>
            <name>Kevin</name>
            <position>Small Forward</position>
        </user>
        <user x="5">
            <team>Boston</team>
            <name>Paul</name>
            <position>Power Forward</position>
        </user>
        <user x="6">
            <team>New York</team>
            <name>Carmelo</name>
            <position>Power Forward</position>
        </user>
        </users>
</stuff>'''

stuff = ET.fromstring(input)
#findall returns a list
l = stuff.findall('users/user')
print 'parsing 2nd snippet\n'
print 'User count:', len(l)

for item in l:
    print 'Name:', item.find('name').text
    print 'Position:', item.find('position').text
    print 'Team:', item.find('team').text

