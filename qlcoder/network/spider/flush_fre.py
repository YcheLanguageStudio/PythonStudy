import urllib.request
import time

start = {}
counter = {}
stop = {}
web = {}
for numb in range (3,11):
    start[numb] = 0;
    counter[numb] = 0;
    stop[numb] = 0;
    url1 = "http://www.qlcoder.com/train/spider3/" + str(numb)
    webtemp = urllib.request.urlopen(url1).read()
    web[numb] = webtemp.decode()
total = 0
for numb in range (3,11):
    total = total + stop[numb]
time.sleep(5)
while(total<8):
    for numb in range (3,11):
        url1 = "http://www.qlcoder.com/train/spider3/" + str(numb)
        webtemp = urllib.request.urlopen(url1).read()
        webdectemp = webtemp.decode()
        if(webdectemp != web[numb]):
            if(start[numb] == 0):
                start[numb] = 1
                web[numb] = webdectemp
            else:
                stop[numb] = 1
        else:
            if(start[numb] == 1 and stop[numb] == 0):
                counter[numb] = counter[numb] + 1
    time.sleep(5)
    total = 0
    for numb in range (3,11):
        total = total + stop[numb]
    print("start:",start)
    print("counter:",counter)
    print("stop:",stop)

print("counter:",counter)#此处最好再sort一下
