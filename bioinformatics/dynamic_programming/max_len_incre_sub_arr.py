class Node:
    def __init__(self, val):
        self.val = val
        self.next_list = []
        self.max_len = 0

    def append(self, next_val):
        self.next_list.append(next_val)

    def is_leaf(self):
        return len(self.next_list) == 0


def max_len_incre_sub_arr(arr):
    node_arr = map(lambda val: Node(val), arr)

    def max_len_incre_sub_arr_detail(beg_idx):
        if node_arr[beg_idx].max_len == 0:
            if beg_idx == len(arr) - 1:
                node_arr[beg_idx].max_len = 1
            else:
                candidates = filter(lambda node: node.val > node_arr[beg_idx].val,
                                    [max_len_incre_sub_arr_detail(i) for i in range(beg_idx + 1, len(arr))])
                if len(candidates) == 0:
                    node_arr[beg_idx].max_len = 1
                else:
                    max_len = max(map(lambda node: node.max_len, candidates))
                    node_arr[beg_idx].max_len = 1 + max_len
                    node_arr[beg_idx].next_list = filter(lambda node: node.max_len == max_len, candidates)

        return node_arr[beg_idx]

    def print_tree(root_node):
        def dfs_detail(node_ref, node_level):
            blank_str = ''.join(["  "] * node_level)[:-1] + '|_' if node_level > 0 else 'root'

            print '%-50s' % (blank_str + str(node_ref.val))
            for child_node in node_ref.next_list:
                dfs_detail(child_node, node_level + 1)

        dfs_detail(root_node, 0)

    max_len_incre_sub_arr_detail(0)
    max_val = max(map(lambda node: node.max_len, node_arr))
    root_node = Node(-1)
    root_node.next_list = filter(lambda node: node.max_len == max_val, node_arr)

    print 'max incre count:', max_val, '\n'
    print_tree(root_node)


if __name__ == '__main__':
    max_len_incre_sub_arr([7, 2, 3, 1, 5, 8, 9, 6])
