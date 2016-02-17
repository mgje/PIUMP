"""Zu einem Artikel von 20min 
verschiedene Kenngrössen zu den Leserreaktion ermitteln. 
WICHTIG: ID des zu untersuchenden Artikels 
direkt im Source Code eingeben."""
## Change story ID 

storyid = "25774941" #Aendern Sie diese ID

from urllib2 import urlopen
from HTMLParser import HTMLParser
import pprint

def count_comment_entries(cm):
    count = 0
    for entry in cm:
        count += 1
    return count


def count_all_entries(cm):
    count = 0
    for entry in cm:
        count += 1
        if "reply" in entry:
            for reply in entry["reply"]:
                count += 1
    return count

def author_hist(cm):
    d = {}
    for entry in cm:
        if entry["author"] in d:
            d[entry["author"]] += 1
        else:
            d[entry["author"]] = 1
            
        if "reply" in entry:
            for reply in entry["reply"]:
                if reply["author"] in d:
                    d[reply["author"]] += 1
                else:
                    d[reply["author"]] = 1
    return d

def max_msg_thread(cm):
    max_msg = 0
    max_thread = 0
    for entry in cm:
        msg_nr = entry["info"]["msg"]
        thread_nr = entry["info"]["thread"]
        if int(thread_nr) > max_thread:
            max_thread = int(thread_nr)
        if int(msg_nr) > max_msg:
            max_msg = int(msg_nr)
        if "reply" in entry:
            for reply in entry["reply"]:
                msg_nr = reply["replyinfo"]["msg"]
                thread_nr = reply["replyinfo"]["thread"]
                if int(thread_nr) > max_thread:
                    max_thread = int(thread_nr)
                if int(msg_nr) > max_msg:
                    max_msg = int(msg_nr)
                    
    return max_thread,max_msg

def thread_msg_numbers(cm):
    msgl = []
    threadl = []
    for entry in cm:
        msgl.append(int(entry["info"]["msg"]))
        threadl.append(int(entry["info"]["thread"]))
        if "reply" in entry:
            for reply in entry["reply"]:
                msgl.append(int(reply["replyinfo"]["msg"]))
                threadl.append(int(reply["replyinfo"]["thread"]))
    return threadl,msgl
        
    

def reply_hist(cm):
    d = []
    for entry in cm:
        count = 0
        if "reply" in entry:
            for rep in entry["reply"]:
                count += 1
        d.append(count)
    return d

def vote_hist(cm):
    vup = []
    vdown = []
    for entry in cm:
        up = int(entry["info"]["data-voteup"])
        down = int(entry["info"]["data-votedown"])
        vup.append(up)
        vdown.append(down)
    return vup,vdown
    

def nr_of_authors(cm):
    return len(author_hist(cm))

def author_with_max_comments(cm):
    hist = author_hist(cm)
    return max(hist,key=hist.get)

def get_max_nr_per_author(cm):
    hist = author_hist(cm)
    return hist[max(hist,key=hist.get)]

def max_replies(cm):
    return max(reply_hist(cm))

def max_vote_up_down(cm):
    vu,vd = vote_hist(cm)
    return max(vu),max(vd)

def taghasattr(key,value,attrs):
    for attr in attrs:
        if attr[0] == key:
            if value in attr[1]:
                return True
    return False

def get_comment_par(attrs):
    d = {}
    for attr in attrs:
        if attr[0] == "id":
            tmp = attr[1].split('_')
            d["thread"] = tmp[0][6:]
            d["msg"] = tmp[1][3:]
        if attr[0] == "data-voteup" or attr[0] == "data-votedown":
            d[attr[0]] = attr[1]
    return d


class ArticleParser(HTMLParser): # derive new HTML parser

    def __init__(self) :        # class constructor
        HTMLParser.__init__(self)  # base class constructor
        self.comments = []        # create an empty list for storing hyperlinks
        self.insidecomment = False
        self.inreplies = False
        self.inentry = False
        self.instroytitle = False
        self.position = "start"
        self.info = None
        self.commentinfo = None
        self.title = ""
        self.content = ""
        self.author =""
        self.time = ""
        self.storytitle = ""
        self.comment = None 
        self.replies = None
        self.divlevel = 0
        self.lilevel = 0
        
        
    def handle_starttag(self, tag, attrs): 
        if tag == "li":
            self.lilevel += 1
            if taghasattr("class","comment",attrs):
                if self.lilevel == 1:
                    self.insidecomment = True
                    self.comment = {}
                    self.info = get_comment_par(attrs)
                elif self.lilevel == 2:
                    self.commentinfo = get_comment_par(attrs)
                        
        elif tag == "h3":
            if taghasattr("class","title",attrs):
                self.position = "title"
        elif tag == "span":
            if taghasattr("class","author",attrs):
                self.position = "author"
            elif taghasattr("class","time",attrs):
                self.position = "time"
            elif self.instroytitle:
                self.position = "storytitle"
        
        elif tag == "p":
            if taghasattr("class","content",attrs):
                self.position = "content"
        elif tag == "div":
            self.divlevel += 1
            if taghasattr("class","entry",attrs) and self.divlevel < 9:
                self.inentry = True
            elif taghasattr("class","replies",attrs):
                self.replies =[]
                self.inreplies = True
            elif taghasattr("class","story_titles",attrs):
                self.instroytitle = True
                    
    def handle_endtag(self, tag):
        if tag == "li":
            self.lilevel -= 1
            if self.lilevel == 0:
                if self.insidecomment:
                    self.comments.append(self.comment)
                self.insidecomment = False
        elif tag == "h3":
            self.position = "out"
        elif tag == "span":
            self.position = "out"
            self.position = "out"
        elif tag == "p":
            if self.position == "content":
                col ={}
                col["author"] = self.author
                col["time"] = self.time
                col["title"] = self.title
                col["content"] = self.content
                if self.inentry:
                    col["info"] = self.info
                    self.comment = col
                if self.inreplies:
                    col["replyinfo"] = self.commentinfo
                    self.replies.append(col)
                self.position = "out"
                
        elif tag == "div":
            self.divlevel -= 1
            if self.divlevel < 8 and self.comment != None:
                if self.inreplies:
                    self.comment["reply"] = self.replies
                self.inentry = False
                self.inreplies = False
            elif self.divlevel < 7 and self.instroytitle:
                self.instroytitle = False
        return
        
    def handle_data(self, data):
        if self.position == "title":
            self.title = data
        elif self.position == "author":
            self.author = data
        elif self.position == "time":
            self.time = data
        elif self.position == "content":
            self.content = data
        elif self.position == "storytitle":
            self.storytitle = data
        return
    
    def get_comments(self) :     # return the list of extracted links
        return self.comments
    
    def get_storytitle(self):
        return self.storytitle

zeitung = 'http://www.20min.ch';

## storyid ist am Anfang definiert !!!

kommentare = zeitung + '/talkbacks/story/' + storyid
story = zeitung + '/schweiz/news/story/' + storyid

# Titel des Artikels zur StoryID einlesen
response = urlopen(story,timeout=3)
html = response.read()
p = ArticleParser()
p.feed(html)
storytitle = p.get_storytitle()

### Kommentare zur Story einlesen
response = urlopen(kommentare,timeout=3)
html = response.read()
p = ArticleParser()
p.feed(html) 

article_comments = p.get_comments()

#pprint.pprint(article_comments)

print "Artikel-Fingerprint"
print "Titel: %s"%storytitle
print "Artikel ID: %s"%storyid
print "URL: %s"%story
print "Anzahl Kommentare und Antworten: %d"% count_all_entries(article_comments)
print "Anzahl Kommentare: %d"% count_comment_entries(article_comments)
print "Anzahl verschiedener Autoren: %d" % nr_of_authors(article_comments)
print "Max Beiträge eines Autors: %d" % get_max_nr_per_author(article_comments)
print "Autor mit den meisten Beiträgen: %s" % author_with_max_comments(article_comments)
print "Max Rückmeldungen auf einen Kommentar: %d" % max_replies(article_comments)
vu,vd = max_vote_up_down(article_comments)
print "Max Up_Votes eines Kommentars: %d" % vu
print "Max Down_Votes eines Kommentars: %d" % vd
mt,mm = max_msg_thread(article_comments)
print "Max Threads: %d " % mt
print "Max MSG NR: %d " % mm
tl,ml = thread_msg_numbers(article_comments)
print "Existing Threads: "
print tl
print "Existing MSG Nr: "
print ml



pprint.pprint(article_comments)