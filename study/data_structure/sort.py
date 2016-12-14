numbers = [5, 2, 9, 7]
numbers.sort(lambda a, b: b - a)
print numbers

my_list = [{u'favs': 1606345, u'id': 413581}, {u'favs': 1606374, u'id': 985991}, {u'favs': 1606329, u'id': 828571}]
my_list.sort(lambda a, b: b[u'favs'] - a[u'favs'])
print my_list
