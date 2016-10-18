def test():
    int_value = 10 ** 5
    str_value = str(int_value)
    len_num = len(str_value)
    len_str = str(len_num)
    if len_num < 10:
        len_str = '0' + len_str
    print str_value
    print len(str_value)
    en_str= len_str + str_value
    print en_str
    print en_str[2:]


def encode(num):
    len_num = len(str(num))
    len_str=str(len_num)
    if len_num<10:
        len_str='0'+len_str

    return len_str+str(num)

def decode(str):
    return int(str[2:])

if __name__ == '__main__':
    test()