from pypinyin import pinyin, lazy_pinyin
import pypinyin

with open('pinyin.txt') as fs:
    strings=fs.readlines()

# print(strings)

for res in strings:
    # print(res)
    print pinyin(res.decode('utf-8'))
