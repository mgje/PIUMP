import urllib2
import pprint
import json
start= "Universitätstrasse 6 ETH Zürich"
ziel= "Zoo Zürich"
start = urllib2.quote(start.encode('utf-8'))
end = urllib2.quote(end.encode('utf-8'))
geocode_url = "https://maps.googleapis.com/maps/api/directions/json?origin=%s&destination=%s&avoid=highways&mode=bicycling" % (start,ziel)
req = urllib2.urlopen(geocode_url)
jsonResponse = json.loads(req.read())
pprint.pprint(jsonResponse) 
#print jsonResponse["results"][0]["formatted_address"]

