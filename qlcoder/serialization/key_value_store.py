import os
import zlib

mp = {}


def write_file(offset, my_bytes):
    with open('key_value_tmp.txt', 'w+') as ofs:
        ofs.seek(offset)
        ofs.write(my_bytes)
    return


def read_file(offset, my_length):
    if not os.path.exists("key_value_tmp.txt"):
        return ''
    with open('key_value_tmp.txt', 'r') as ifs:
        ifs.seek(offset)
        return ifs.read(my_length)


def get(key):
    return mp.get(key, 0)


def put(key):
    mp[key] = mp.get(key, 0) + 1
    s = ''
    for kv in mp.items():
        s = '%s:%d\n' % kv + s
    b_s = bytearray(s)
    write_file(0, b_s)


def init():
    bytes_arr = read_file(0, 102400)
    print bytes_arr, len(bytes_arr)
    for li in bytes_arr.split('\n'):
        l2 = li.split(':')
        if len(l2) < 2:
            print l2, len(l2), li
            continue
        mp[l2[0]] = int(l2[1])


init()
for i in range(1, 10):
    put(50 * chr(i + 96))

encoded_str = zlib.compress(50 * chr(1 + 96))
print len(encoded_str)
decoded_str = zlib.decompress(encoded_str)
print len(decoded_str)
