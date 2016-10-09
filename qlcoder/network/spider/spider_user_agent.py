import urllib.request as request

url="http://www.qlcoder.com/train/secret"
myRequest = request.Request(url)
myRequest.add_header('User-Agent' , 'qlcoder spide')
page = request.urlopen(myRequest).read().decode("utf-8")

print (page)