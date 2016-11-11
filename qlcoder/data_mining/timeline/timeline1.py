import random
import sys
import hashlib
import numpy
import string

global_digest_list = list()
if sys.version_info[0] == 3:
    print ("Welcome to qlcoder!")
    print ("We find your Python version is python3.X")
    print ("But this script needs to be executed with Python2.X\n")
    exit()

random.seed(10)
limit = 10000000
vertex_list = numpy.ndarray(limit + 1)
vertex_list = map(lambda ele: [], vertex_list)


def compute_md5(str_list):
    res_str = '-'.join(str_list)
    return hashlib.md5(res_str).hexdigest()


def verbose_time_line(vertex_index):
    if len(vertex_list[vertex_index]) == 0:
        global_digest_list.append(hashlib.md5("").hexdigest())
    else:
        vertex_list[vertex_index].reverse()
        if len(vertex_list[vertex_index]) == 1:
            global_digest_list.append(hashlib.md5(vertex_list[vertex_index][0]).hexdigest())
        else:
            global_digest_list.append(compute_md5(vertex_list[vertex_index]))
        vertex_list[vertex_index] = list()


def notify_message(vertex_index, message_str):
    times_count = 2
    notified_vertex_index = times_count * vertex_index
    while notified_vertex_index < limit + 1:
        vertex_list[notified_vertex_index].append(message_str)
        times_count += 1
        notified_vertex_index = times_count * vertex_index


for i in range(limit):
    r = random.randint(1, limit)
    if i < 10:
        print r
    if i % 3 == 0:
        message_str = ''.join(random.sample(string.ascii_letters, 4))
        notify_message(r, message_str)
    else:
        verbose_time_line(r)

print 'Over'

print compute_md5(global_digest_list)

with open('time_line_res.txt', 'w') as ofs:
    for my_str in global_digest_list:
        ofs.write('-')
        ofs.write(my_str)
