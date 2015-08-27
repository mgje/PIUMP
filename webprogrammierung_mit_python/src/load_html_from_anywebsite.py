from urllib2 import urlopen

endpoint = "http://www.tigerjython.ch"
html = urlopen(endpoint).read()

print(html)

