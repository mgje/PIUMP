import urllib2
import pprint
import json
import re

TAG_RE = re.compile(r'<[^>]+>')

def remove_tags(text):
    return TAG_RE.sub('', text)

start = "Universitätstrasse 6 ETH Zürich"
ziel = "Zoo Zürich"
sprache = "de" # "en"
art = "walking" #driving walking transit bicycling
start = urllib2.quote(start.encode('utf-8'))
ziel = urllib2.quote(ziel.encode('utf-8'))

geocode_url = "https://maps.googleapis.com/maps/api/directions/json?origin=%s&destination=%s&avoid=highways&mode=%s&language=%s" % (start,ziel,art,sprache)
req = urllib2.urlopen(geocode_url)
jsonResponse = json.loads(req.read())

print "Distanz:" + jsonResponse['routes'][0]['legs'][0]['distance']['text']
print "Dauer:" + jsonResponse['routes'][0]['legs'][0]['duration']['text']

for step in jsonResponse['routes'][0]['legs'][0]['steps']:
    print step['distance']['text'] + " > "+ remove_tags(step['html_instructions'])


