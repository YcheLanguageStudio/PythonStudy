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


def demo_bimap():
    my_bimap = LetterIndexBimap()
    print my_bimap.char2index('c')
    print my_bimap.index2char(1)
    my_ch = 'e'
    print ord(my_ch) - ord('a')
    print my_bimap.index2char(13)


def demo_dict():
    adj_list_dict = {1: [2, 3], 2: [1, 3], 3: [1, 2, 4], 4: [3]}
    for key in adj_list_dict:
        adj_list_dict[key] = set(adj_list_dict[key])

    my_dict = dict([(vertex, adj_list_dict[vertex] | {vertex}) for vertex in adj_list_dict])
    print my_dict


if __name__ == '__main__':
    demo_bimap()
    demo_dict()
