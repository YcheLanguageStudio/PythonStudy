import mmap
import os
import struct

KEY_FILENAME = 'key_redis.txt'
VALUE_FILENAME = 'value_redis.txt'

mp = {}
next_key_idx = 0
next_val_idx = 0
key_mmap = None
val_mmap = None


def get(key):
    return mp[key][0]


def put(key):
    global next_key_idx
    global next_val_idx
    global key_mmap
    global val_mmap
    if mp.__contains__(key):
        mp[key][0] += 1
        val_mmap[mp[key][1]] = struct.pack('B', mp[key][0])
    else:
        key_mmap.resize(next_key_idx + len(key) + 1)
        key_mmap[next_key_idx: next_key_idx + len(key) + 1] = key + '\n'
        next_key_idx += len(key) + 1

        val_mmap.resize(next_val_idx + 1)
        val_mmap[next_val_idx] = struct.pack('B', 1)
        next_val_idx += 1
    return


def init():
    if not os.path.exists(KEY_FILENAME):
        os.mknod(KEY_FILENAME)
    if not os.path.exists(VALUE_FILENAME):
        os.mknod(VALUE_FILENAME)

    global next_key_idx
    global next_val_idx
    key_file_size = os.path.getsize(KEY_FILENAME)
    val_file_size = os.path.getsize(VALUE_FILENAME)
    if key_file_size == 0:
        with open(KEY_FILENAME, 'w') as ofs:
            ofs.truncate(1)
            key_file_size = 1
            next_key_idx = 0
    else:
        next_key_idx = key_file_size
    if os.path.getsize(VALUE_FILENAME) == 0:
        with open(VALUE_FILENAME, 'w') as ofs:
            ofs.truncate(1)
            val_file_size = 1
            next_val_idx = 0
    else:
        next_val_idx = val_file_size

    global key_mmap
    global val_mmap
    key_mmap = mmap.mmap(os.open(KEY_FILENAME, os.O_RDWR), key_file_size)
    val_mmap = mmap.mmap(os.open(VALUE_FILENAME, os.O_RDWR), val_file_size)

    key_list = []
    if next_key_idx != 0:
        key_list = filter(lambda x: len(x) != 0 and x != '\x00', key_mmap[0:len(key_mmap)].split('\n'))

    for idx in range(0, len(key_list)):
        mp[key_list[idx]] = [struct.unpack('B', val_mmap[idx])[0], idx]


def some_get_put():
    put('www.baidu.com')
    put('www.google.com')
    put('blog.cheyulin.me')
    print get('www.google.com')
    print get('www.baidu.com')
    print get('blog.cheyulin.me')


if __name__ == '__main__':
    init()
    some_get_put()
