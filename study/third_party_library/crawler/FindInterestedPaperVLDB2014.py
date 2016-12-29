import urllib2
import gzip
import re
import sys
from StringIO import StringIO
from bs4 import BeautifulSoup

__author__ = 'cheyulin'


def loadData(url):
    request = urllib2.Request(url)
    request.add_header('Accept-encoding', 'gzip')
    response = urllib2.urlopen(request)
    print response.info().get('Content-Encoding')
    if response.info().get('Content-Encoding') == 'gzip':
        print 'response data is in gzip format.'
        buf = StringIO(response.read())
        f = gzip.GzipFile(fileobj=buf)
        data = f.read()
    else:
        data = response.read()
    return data


if __name__ == '__main__':
    reload(sys)
    i = 0;
    sys.setdefaultencoding('utf-8')
    path = r'/home/cheyulin/Documents/Paper/GraphInDB/vldb2013/'
    page = loadData('http://www.vldb.org/pvldb/vol6.html')
    # path = r'/home/cheyulin/Documents/Paper/GraphInDB/vldb2014/'
    # page = loadData('http://www.vldb.org/pvldb/vol7.html')
    # path = r'/home/cheyulin/Documents/Paper/GraphInDB/vldb2016/'
    # page = loadData('http://www.vldb.org/pvldb/vol9.html')
    soup = BeautifulSoup(page, from_encoding='utf-8')
    paper_info = soup.find_all('a');
    for paper in paper_info:
        if re.match(r'.*http.*pdf.*', str(paper)):
            paper_file_name = str(paper.string).strip().replace(' ', '_') + '.pdf'
            if re.match('.*[Gg]raph.*', paper_file_name):
                i += 1
                paper_url = paper['href']
                print "hi:" + str(paper).split('</a>')[0].split(' ')[2].strip()
                print paper_file_name
                print str(paper_url).strip()
                f = urllib2.urlopen(paper_url)
                with open(path + paper_file_name, 'wb') as output_stream:
                    output_stream.write(f.read())
    print i
