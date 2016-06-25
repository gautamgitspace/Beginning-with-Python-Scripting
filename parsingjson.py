#JSON PARSING - JSON represents data as nested lists and dictionaries - *super benefical*

#example - dictionary
import json
data = '''
{
  "name" : {
  "firstName" : "Allen",
  "lastName" : "Iverson"},
  "position" : {
    "main" : "Point Guard",
    "alternate" : "Small Forward"
   },
   "email" : {
     "hide" : "yes"
   }
}'''
print '\n#1 example - dictionary\n'
info = json.loads(data)
print 'Name:', info["name"]["lastName"]
print 'Position:', info["position"]["main"]

#example - list
print '\n#2 example - list\n'
input = '''
[
  { "player" : "Kyrie Irving",
    "team" : "CLE",
    "pos" : "Point Guard"
  } ,
  { "player" : "LeBron James",
    "team" : "CLE",
    "pos" : "Power Forward"
  }
]'''

info = json.loads(input)
print 'User count:', len(info)

for item in info:
    print 'Player:', item['player']
    print 'Team:', item['team']
    print 'Position:', item['pos']

