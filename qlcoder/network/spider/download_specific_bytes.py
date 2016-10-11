import urllib2

req = urllib2.Request('http://www.python.org/')
req.add_header('Range', 'bytes=0-20') # set the range, from 0byte to 19byte, 20bytes len
res = urllib2.urlopen(req)

data = res.read()

print data
print '---------'
print 'len:%d'%len(data)
