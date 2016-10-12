import requests

url = 'https://mail.163.com/entry/cgi/ntesdoor?funcid=loginone&passtype=1&product=mail163'
s = requests.Session()
params = {  'username':'aiiowjw095686@163.com-',
            'password':'----lmm9806'
            }

s.post(url, params = params)
r = s.get('https://reg.163.com/account/accountInfo.jsp')

print(r.text) # to find it
