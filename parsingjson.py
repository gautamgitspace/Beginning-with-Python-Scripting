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

info = json.loads(data)
print 'Name:', info["name"]["lastName"]
print 'Position:', info["position"]["main"]
