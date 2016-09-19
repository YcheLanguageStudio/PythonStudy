class LetterIndexBimap:
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


if __name__ == '__main__':
    my_bimap = LetterIndexBimap()
    print my_bimap.char2index('c')
    print my_bimap.index2char(1)
    my_ch='e'
    print ord(my_ch) - ord('a')
    print my_bimap.index2char(13)
