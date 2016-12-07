def gcd_euclidean(lhs, rhs):
    if rhs == 0:
        return lhs
    else:
        return gcd_euclidean(rhs, lhs % rhs)


# val from 0 to 25
def encrypt(letter_index, k0, k1):
    return (letter_index * k0 + k1) % 26


class EngIndexBiMap:
    def __init__(self):
        self.char2index_dict = dict()
        self.index2char_dict = dict()
        for i in range(0, 25):
            self.char2index_dict[chr(ord('a') + i)] = i
            self.index2char_dict[i] = chr(ord('a') + i)

    def char2index(self, ch):
        return self.char2index_dict[ch]

    def index2char(self, index):
        return self.index2char_dict[index]


def cipher(msg, k0, k1):
    my_bimap = EngIndexBiMap()
    cipher_text = map(lambda ele: my_bimap.index2char(encrypt(my_bimap.char2index(ele), k0, k1)), msg)
    return cipher_text


if __name__ == '__main__':
    print 'Demo gcd of 24 and 36 is:' + str(gcd_euclidean(24, 36)) + '\n'

    cipher_text = cipher('lecture', 3, 1)
    print cipher_text
    print ''.join(cipher_text)
