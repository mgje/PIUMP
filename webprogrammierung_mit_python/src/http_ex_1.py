from httplib import HTTPConnection

conn = HTTPConnection("www.tigerjython.ch")

conn.request("GET","/index.html")
res = conn.getresponse()
print res.status, res.reason 

for header in res.getheaders():
    print(header[0]+" : "+header[1])

conn.close()