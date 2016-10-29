import urllib2
import json

whole_list = []
start_num = 46364
for table_index in range(0, 10):
    for offset in range(0, 600, 100):
        url = 'http://www.qlcoder.com/train/mysql?table={}&a={}&b={}'.format(table_index, start_num + offset, 100)
        print url
        request = urllib2.Request(url)
        response_stream = urllib2.urlopen(request, timeout=200)
        json_obj = json.load(response_stream)
        whole_list.extend(json_obj['data'])
        print whole_list
        print len(whole_list)

print whole_list

whole_list.sort(lambda left, right: right[u'favs'] - left[u'favs'])

print whole_list

my_sum = 0
for i in range(3000, 3020):
    my_sum += whole_list[i][u'favs']

print my_sum
