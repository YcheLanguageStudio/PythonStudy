import copy


class HuffmanNode:
    def __init__(self, freq, letter=None):
        self.left_node = None
        self.right_node = None
        self.frequency = freq
        self.letter = letter

    def __str__(self):
        if self.letter is not None:
            return str(self.frequency) + '\t' + " '" + self.letter + "'"
        else:
            return str(self.frequency) + '\t' + 'branch node'


def get_initial_huffman_nodes():
    with open('freq.txt') as fs:
        freq_strings = fs.readlines()

    ret_huffman_nodes = list()
    for ele in freq_strings:
        strings = ele.split('=')
        my_ch = strings[0][2]
        my_num = int(strings[1].split(')')[0].lstrip().rstrip())
        ret_huffman_nodes.append(HuffmanNode(my_num, my_ch))

    ret_huffman_nodes.sort(key=lambda k: k.frequency)
    return ret_huffman_nodes


def reduce_two_huffman_nodes(my_huffman_nodes, i, j):
    new_node = HuffmanNode(my_huffman_nodes[i].frequency + my_huffman_nodes[j].frequency)
    new_node.left_node = my_huffman_nodes[i]
    new_node.right_node = my_huffman_nodes[j]

    my_huffman_nodes.remove(new_node.left_node)
    my_huffman_nodes.remove(new_node.right_node)
    my_huffman_nodes.append(new_node)
    my_huffman_nodes.sort(key=lambda k: k.frequency)


def process_huffman_nodes(my_huffman_nodes, tmp_result_list):
    if my_huffman_nodes[0].frequency == my_huffman_nodes[1].frequency:
        max_same_index = 1
        for i in range(2, len(my_huffman_nodes)):
            if my_huffman_nodes[i].frequency == my_huffman_nodes[1].frequency:
                max_same_index = i
        for i in range(0, max_same_index + 1):
            for j in range(0, max_same_index + 1):
                if i != j:
                    copy_my_huffman_nodes = copy.copy(my_huffman_nodes)
                    reduce_two_huffman_nodes(copy_my_huffman_nodes, i, j)
                    tmp_result_list.append(copy_my_huffman_nodes)
    else:
        if len(my_huffman_nodes) > 2 and my_huffman_nodes[1].frequency == my_huffman_nodes[2].frequency:
            max_same_index = 2
            for i in range(3, len(my_huffman_nodes)):
                if my_huffman_nodes[i].frequency == my_huffman_nodes[1].frequency:
                    max_same_index = i
            for i in range(1, max_same_index + 1):
                copy_my_huffman_nodes = copy.copy(my_huffman_nodes)
                reduce_two_huffman_nodes(copy_my_huffman_nodes, 0, i)
                tmp_result_list.append(copy_my_huffman_nodes)
        else:
            copy_my_huffman_nodes = copy.copy(my_huffman_nodes)
            reduce_two_huffman_nodes(copy_my_huffman_nodes, 0, 1)
            tmp_result_list.append(copy_my_huffman_nodes)


def build_huffman_tree(huffman_node_list):
    result_list = list()
    result_list.append(huffman_node_list)
    while len(result_list[0]) > 1:
        print len(result_list[0]), ',len_res:',len(result_list)
        frontier_list = list()
        for tmp_huffman_nodes in result_list:
            process_huffman_nodes(tmp_huffman_nodes, frontier_list)
        result_list = frontier_list
    result_list = map(lambda my_list: my_list[0], result_list)
    return result_list


# pre order traversal
def dfs(tree):
    if tree.left_node is None and tree.right_node is None:
        print tree
    else:
        print tree
        print 'left:'
        dfs(tree.left_node)
        print 'right:'
        dfs(tree.right_node)
        print '--'


def recover_message(candidate_tree):
    encoded_text = '1001111111100111111010011110110011111000101001110110010111110000110010001110101111011100001011111111001000101010010001010111100110100110011100111000011011000111010011010110011111011110101100011110101100100111111000010110111000010001000010101111011100001011101101010010001111100110101110011101000011001110011100010010110110001110101111001001110001011011100001000100001110100011111010110100101011110000110101111111110110111111110010111111001001001000101011110000100100010101001001011111111001111110100011101011110111000001010111100010011010110111010010010110001101101011001001110001011011100001000100000110111011000110000010101111000100110110001111001101101000100010101001000011010111101000101011110000110001001111011000100111011001001110001011011100001000100000100011110011110011010010001010100100010010011111010010001110001100111001110001111100011110010111101100100111001000110011001110101111010001010110111110110001001000011110100011101011110100100101000110001111101010101101010101011100100111001000110011001110101111010001101100011101001101011110111000001111010100011101011110100011011000010001000101110010011100100011001100111010111101001111110011111000110100111010111000111000111110111111100111000101001010010000110010000111101001011110001110101111010010011011110010010010111111100111010111101000100011101100101111100011101011100011100011111011110000111101001100010100111010111101001001010000110110101111111001110101111010010111111011000101000111010111000111000011011000111110101101010100111010111101000101010011011101111110001101110000101111111100111010111101000101101101111101010010010001110101110001110000110011111001100011000100100101001110101111010011000110110000100110011001111011111100011001111011010110010011100111110000100110110010011001101001100111001110000100011111111101101001000101010010001011111101010111101100000111011110001110101111010010100111011001011111000011011000111010011010111111111001111110111101100000111010110111010100101001110110010111110001000101010010001000010001000011101011110100101001110110010111110010100111011110001001101111011001111011100100011101011110100100010100101011011101110000001110101000110101111010111011011100001110101100110111101100110111101001100110010'
    tmp_node = candidate_tree
    for idx in range(0, len(encoded_text)):
        if tmp_node.left_node is None and tmp_node.right_node is None:
            print tmp_node.letter,
            tmp_node = candidate_tree
        if encoded_text[idx] == '1':
            tmp_node = tmp_node.right_node
        else:
            tmp_node = tmp_node.left_node

    if tmp_node.left_node is None and tmp_node.right_node is None:
        print tmp_node.letter,
    print '\n'


if __name__ == '__main__':
    huffman_nodes = get_initial_huffman_nodes()
    final_result_list = build_huffman_tree(huffman_nodes)

    for res_huffman_tree in final_result_list:
        recover_message(res_huffman_tree)
        # dfs(res_huffman_tree)
