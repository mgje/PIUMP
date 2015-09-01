""" HEAD News ser Rubrik Digital von 20min ermitteln und ausgeben """
from HTMLParser import HTMLParser
import urllib2

class DigitalHeadLine(HTMLParser):
    
    capture_txt=False
    headlines =[]
    

    def handle_starttag(self, tag, attrs):
        if tag == "h2":
            if "data-vr-contentbox" in dict(attrs):
                self.capture_txt=True
        return      
        
    
    def handle_endtag(self, tag):
        if tag == "h2":
             if self.capture_txt == True:
                self.capture_txt=False
        return
    
    def handle_data(self, data):
        if self.capture_txt == True:
            self.headlines.append(data)
        return
    
    def getheadlines(self):
        print self.headlines[0]
            
            
url="http://www.20min.ch/digital/"
res = urllib2.urlopen(url)        
encoding = "iso-8859-1"
html = res.read().decode(encoding)   
parser = DigitalHeadLine()
parser.feed(html)
parser.getheadlines()
