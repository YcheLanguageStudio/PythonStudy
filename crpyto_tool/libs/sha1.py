import math

md_buffer = ['67452301', 'efcdab89', '98badcfe', '10325476', 'c3d2e1f0']
magic_num_list = [2, 3, 5, 10]
magic_num_str_list = map(lambda ele: hex(int(2 ** 30 * math.sqrt(ele)))[2:], magic_num_list)


def get_magic_number(t):
    if t > 80 or t < 0:
        print 'error'
        return None
    else:
        return magic_num_list[t / 20]


def get_function(t):
    if t > 80 or t < 0:
        print 'error'
        return None
    elif t < 20:
        return lambda b, c, d: (b & c) | (c & d)
    elif t < 40:
        return lambda b, c, d: b ^ c ^ d
    elif t < 60:
        return lambda b, c, d: (b & c) | (b & d) | (c & d)
    else:
        return lambda b, c, d: b ^ c ^ d


# Rotate left: 0b1001 --> 0b0011
def shift_left(val, r_bits, max_bits):
    return (val << r_bits % max_bits) & (2 ** max_bits - 1) | (
        (val & (2 ** max_bits - 1)) >> (max_bits - (r_bits % max_bits)))


# Rotate right: 0b1001 --> 0b1100
def shift_right(val, r_bits, max_bits):
    return ((val & (2 ** max_bits - 1)) >> r_bits % max_bits) | (
        val << (max_bits - (r_bits % max_bits)) & (2 ** max_bits - 1))


print md_buffer
print magic_num_str_list
