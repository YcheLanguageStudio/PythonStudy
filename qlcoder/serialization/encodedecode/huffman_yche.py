import numpy as np


class HuffmanNode:
    def __init__(self, freq, letter=None):
        self.left_node = None
        self.right_node = None
        self.frequency = freq
        self.letter = letter

    def __str__(self):
        if self.letter != None:
            return str(self.frequency) + '\t' + " '" + self.letter + "'"
        else:
            return str(self.frequency) + '\t' + 'branch node'


freq_strings = list()
with open('freq.txt') as fs:
    freq_strings = fs.readlines()

huffman_nodes = list()
for ele in freq_strings:
    strings = ele.split('=')
    yche_ch = strings[0][2]
    yche_num = int(strings[1].split(')')[0].lstrip().rstrip())
    huffman_nodes.append(HuffmanNode(yche_num, yche_ch))

huffman_nodes.sort(key=lambda k: k.frequency)
print len(huffman_nodes)

while len(huffman_nodes) > 1:
    new_node = HuffmanNode(huffman_nodes[0].frequency + huffman_nodes[1].frequency)
    new_node.left_node = huffman_nodes[0]
    new_node.right_node = huffman_nodes[1]
    huffman_nodes.append(new_node)

    huffman_nodes.remove(huffman_nodes[0])
    huffman_nodes.remove(huffman_nodes[1])
    huffman_nodes.sort(key=lambda k: k.frequency)

    print len(huffman_nodes)

final_tree = huffman_nodes[0]

#middle order traversal
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

dfs(final_tree)
