import re

yche_str = ['1', '2', '3']
yche_str.reverse()
print yche_str

print '-'.join(yche_str)

my_str = 'The Answer is haha'
if re.match('.*[A-a]nswer.*', my_str):
    print my_str
else:
    print 'bad'
