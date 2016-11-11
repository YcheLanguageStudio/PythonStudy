import os

mp = {}
append_offset = 0

FILENAME = 'key_value_tmp.txt'


def write_file(offset, my_bytes):
    with open(FILENAME, 'r+') as ofs:
        ofs.seek(offset)
        ofs.write(my_bytes)
    return


def read_file(offset, my_length):
    if not os.path.exists(FILENAME):
        os.mknod(FILENAME)
        os.ftruncate(os.open(FILENAME, os.O_RDWR), 102400)
        return ''
    with open(FILENAME, 'r') as ifs:
        ifs.seek(offset)
        return map(ord, ifs.read(my_length))


def get(key):
    if not mp.__contains__(key):
        return 0
    return mp[key][0]


def put(key):
    if mp.__contains__(key):
        mp[key][0] += 1
        write_file(mp[key][1],  chr(mp[key][0]))
    else:
        global append_offset
        to_be_write = bytearray(key + chr(1) + '\0')
        write_file(append_offset, to_be_write)
        append_offset += len(key) + 2
        mp[key] = [1, append_offset - 1]


def init():
    bytes_arr = ''.join(map(chr, read_file(0, 102400)))
    key_val_list = filter(lambda x: len(x) > 0, bytes_arr.split('\0'))
    val_offset = 0
    global append_offset
    for idx in range(0, len(key_val_list)):
        key = key_val_list[idx][0:len(key_val_list[idx]) - 1]
        val = ord(key_val_list[idx][len(key_val_list[idx]) - 1])
        val_offset += len(key)
        mp[key] = [val, val_offset]
        val_offset += 2
        append_offset += len(key_val_list[idx]) + 1


def some_get_put():
    put('50')
    put('github.com')
    put('www.baidu.com')
    put('www.google.com')
    put('blog.cheyulin.me')
    print get('www.google.com')
    print get('www.baidu.com')
    print get('blog.cheyulin.me')
    print get('github.com')
    print get('50')

if __name__ == '__main__':
    init()
    print mp
    some_get_put()
