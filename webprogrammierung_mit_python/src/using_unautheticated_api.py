import json
#from urllib2 import Request
from urllib2 import urlopen
endpoint = "https://api.github.com/users/joelgrus/repos"


repos = json.loads(urlopen(endpoint).read())
print repos

#req = Request(endpoint)
#handler = urlopen(req)

#print handler.getcode()
#print handler.headers.getheader('content-type')

## Read from Github

#print urlopen(endpoint).read()
