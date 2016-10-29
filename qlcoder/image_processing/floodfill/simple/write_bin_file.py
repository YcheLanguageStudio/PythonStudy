import struct

bytes_list = list()
with open('foo_output', 'wb') as output_stream:
    with open('foo') as input_stream:
        bytes_list = input_stream.readlines()[0]
        print bytes_list
        bytes_list = bytes_list[1:len(bytes_list) - 1]
        print bytes_list
        bytes_list = bytes_list.split(',')
        for ele in bytes_list:
            ele = ele.lstrip().rstrip()
            ele = int(ele)
            print type(ele), ele
            my_bytes = struct.pack('B', ele)
            output_stream.write(my_bytes)
            print ele
        print len(bytes_list)
