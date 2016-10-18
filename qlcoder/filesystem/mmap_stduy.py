mp = {}
# user_code
def get(key):
    return mp.get(key, 0)

def put(key):
    mp[key] = mp.get(key, 0)+1
    s = ''
    for kv in mp.items():
        s = '%s:%d\n' % kv + s
    b_s = bytearray(s)
    write_file(0, b_s)


def init():
    ls = map(chr, read_file(0, 102400))
    for li in ''.join(ls).split('\n'):
        l2 = li.split(':')
        if len(l2)<2:
            continue
        mp[l2[0]] = int(l2[1])
