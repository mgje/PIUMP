"""Informationen (strukturiert, JSON) zu einem Github-Projekt anfordern"""
import json
import pprint

from urllib2 import urlopen
endpoint = "https://api.github.com/users/mgje/events"

repos = json.loads(urlopen(endpoint).read())
pprint.pprint(repos) 

