import re
from collections import Counter, defaultdict
import jieba

with open('santi.txt', 'rb') as fh:
    content = fh.read()
    letter_reg = re.compile(ur'[\u4e00-\u9fa5]{1}', re.UNICODE)
    letters_map = Counter(letter_reg.findall(content.decode('utf8')))
    words_map = defaultdict(int)
    for word in jieba.cut(content):
        if len(word) == 2:
            words_map[word] += 1
    print words_map

    m = {k: float(count)/(letters_map[k[0]]*letters_map[k[1]]) for k,count in words_map.iteritems() if count>=100}
    rank = sorted(m.iteritems(), lambda x, y: cmp(x[1], y[1]), reverse=True)
    for i in rank:
        print i[0].encode('utf8'), i[1]
