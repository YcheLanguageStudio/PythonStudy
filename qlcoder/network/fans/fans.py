import hashlib
import urllib.request

i = 0
k = 1
while True:
    i += 1
    b = hashlib.md5()
    a = "20161013cheyulin" + str(k) + str(i)
    b.update(a.encode())
    if (b.hexdigest()[0:6] == "000000"):
        print(i, a, b.hexdigest())
        req = urllib.request.Request(
            "http://www.qlcoder.com/train/handsomerank?_token=3LAlZVysfo1JXJRQPXudmXRHgHPCtYJoY1jNgZu7&user=cheyulin&checkcode=" + str(i))
        urllib.request.urlopen(req)
        k += 1
        i = 0