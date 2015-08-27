from urllib2 import urlopen

conn = urlopen("http://www.tigerjython.ch")
status = conn.getcode()
reason = conn.msg

print(status,reason)
print(conn.headers)

conn.close()