""" HTTP-Anfrage und den Inhalt der Antwort (Response body) ausgeben"""
from urllib2 import urlopen
endpoint = "http://www.tigerjython.ch"
response = urlopen(endpoint)
html = response.read()
print(html)