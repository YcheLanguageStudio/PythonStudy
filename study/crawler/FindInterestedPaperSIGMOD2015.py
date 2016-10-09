import urllib2
import gzip
import re
import sys
import time
from StringIO import StringIO
from bs4 import BeautifulSoup

__author__ = 'cheyulin'


def loadData(url):
    request = urllib2.Request(url)
    # Mimic Mozilla
    request.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:43.0) Gecko/20100101 Firefox/43.0')
    request.add_header('Accept-encoding', 'gzip')
    request.add_header('Cookie',
                       'NID=75=vOEsJkd-HYc3USa1AKTdFU5IDwUKC3CV8vW_HAZzelym_J3HMVTaTRTJ5q8V2Cq7lSamBOXaGAIQPrwVR-qTcEwGUOmgo9LBoDBE4--QRsXSx3ehj-zk9YwemsoQoZ_ZNYMhcIw1hG52oXrtoBMNtMUXIulVpoQYpF2HsSYM1xn41Kw2w_sjslVI22CEJt6u2RE995UxcNwsYaUKfWOOHlHDVAZLwDQzr2dO6a-tF4khs3XjQ8NqGC4IFIEjDAiB6RmmHCMKjKseDNaAaeO_yrKhE3ga; SID=DQAAAAsBAACFoMeZri2WlB4U5FiKpjKIYwIkA6__A8u1smIKAfSFo8KeOBQ-Wjr8ecDcHGTD2m3baIQ3iBdvleWP1dDOblnmApTrrL-yiXO2CPh-OBlslMDoO7sKDHpF0GrU_YaZuw2Mu9h9-2ILyxiF2QheLlbx5scVeijZIo7TvMl04Oh4rbIfdXkyn7rsMGgvNTJx1cLkOPj5BhWKdS__R1sB5Sfvlcw2nWLij0p3a2beRf-JSYHR_1PnoT0IF2Zw9s7INJEU6kxHCnkwcjG8r9FjbH1tr3OQ4vHrLwALJdLLDyz7JNvkTPtRU2deilFUkOtm9YICZP-2TQH-nlVqADRxBZhtxW4j-Lxhvifc41nlue77TA; HSID=ASLlUqwyRia5aOcYx; SSID=A74xyUhtx9sf4sXdG; APISID=xZI7z53B1Ki0uc9e/AYz9AXVIViF4STwbj; SAPISID=Nrlfz20vqjLQprxL/AXHgIblvNtFQCLZOS; GSP=LM=1445846737:S=x-bES4gCy2NoXLjW')
    response = urllib2.urlopen(request, timeout=20)
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
    i = 0
    sys.setdefaultencoding('utf-8')
    # urllib2.install_opener(urllib2.build_opener(urllib2.HTTPHandler(debuglevel=1)))
    path = r'/home/cheyulin/Documents/Paper/GraphInDB/sigmod2015/'
    page = loadData('http://www.sigmod2015.org/toc_sigmod.shtml')
    soup = BeautifulSoup(page, from_encoding='utf-8')
    paper_info = soup.find_all('a', {'class': 'DLtitleLink'});
    for paper in paper_info:
        # print paper
        paper_name = str(paper.string).strip()
        query_url = "https://scholar.google.com.hk/scholar?q=" + paper_name.replace(' ', '+');
        if re.match('.*[Gg]raph.*', paper_name):
            i += 1
            paper_url = str(paper['href']).strip()
            print query_url
            download_page = loadData(query_url)
            download_soup = BeautifulSoup(download_page, from_encoding='utf-8')
            # print download_soup.prettify()
            link = download_soup.find_all('h3', {'class': 'gs_rt'})[0]
            download_url = link.contents[0]['href']
            print download_url
            paper_file_name = paper_name.replace(' ', '_').replace(r'/', '_') + '.pdf'
            print paper_file_name

            download_page = loadData(download_url)
            download_soup = BeautifulSoup(download_page, from_encoding='utf-8')
            download_link = download_soup.find_all('a', {'title': 'FullText PDF'})[0]['href']
            download_link = 'http://dl.acm.org/' + str(download_link)
            print download_link + '\n'
            time.sleep(3)
            f = urllib2.urlopen(download_link)
            with open(path + paper_file_name, 'wb') as output_stream:
                output_stream.write(f.read())
            time.sleep(3)
print 'Paper Num:' + str(i)
