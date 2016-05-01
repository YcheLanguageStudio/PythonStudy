import urllib2
import gzip
import re
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
    page = loadData('http://www.vldb.org/2015/program/lib/FullProgram.html#D1F1045T1215R5')
    soup = BeautifulSoup(page, from_encoding='GB18030')
    paper_info = soup.find_all('div', {'class': 'booklet_paper_folded'});
    path = r'/home/cheyulin/Documents/Paper/GraphInDB/'
    for paper in paper_info:
        info = paper.findAll('strong')
        title = info[0]
        if re.match(r'.*Graph.*', str(title)):
            pdf_img = paper.findAll('img', {'class': 'paper_controls'})
            if re.match(r'.*http.*pdf.*', str(pdf_img)):
                paper_file_name = str(title).replace('<strong>', '').replace('</strong>', '').replace(' ', '_') + '.pdf'
                print paper_file_name
                paper_url = re.search(r'http.*[^"]pdf', str(pdf_img)).group(0)
                print paper_url
                f = urllib2.urlopen(paper_url)
                with open(path + paper_file_name, 'wb') as output_stream:
                    output_stream.write(f.read())
                    # print soup.prettify().encode('GB18030')
