import urllib2

req = urllib2.Request('http://www.qlcoder.com/download/hugefile')
req.add_header('Range', 'bytes=12345678901-12345678999') # set the range, from 0byte to 19byte, 20bytes len
res = urllib2.urlopen(req)

data = res.read()

print data
print '---------'
print 'len:%d'%len(data)
