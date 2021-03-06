class EndIdx:
    def __init__(self, val=-1):
        self.val = val


class InEdgeLabel:
    def __init__(self, start_idx=-1, end_idx_ref=None):
        """
        :type end_idx_ref: EndIdx
        """
        self.start_idx = start_idx
        self.end_idx_ref = end_idx_ref

    def sub_str(self, whole_str):
        return '' if self.start_idx == -1 else whole_str[self.start_idx:self.end_idx_ref.val + 1]

    def edge_len(self):
        return 0 if self.start_idx == -1 else self.end_idx_ref.val - self.start_idx + 1


class SuffixNode:
    def __init__(self, suffix_link, start_idx=-1, end_idx_ref=None, suffix_idx=-1):
        self.children_dict = {}
        self.suffix_link = suffix_link
        self.edge_label = InEdgeLabel(start_idx, end_idx_ref)
        self.suffix_idx = suffix_idx

    def is_leaf(self):
        return len(self.children_dict) == 0


class ActivePoint:
    def __init__(self, active_node, active_edge, active_len):
        """
        :type active_node: SuffixNode
        """
        self.active_node = active_node
        self.active_edge = active_edge
        self.active_len = active_len

    def walk_down_if_possible(self, cur_node):
        """
        :type cur_node: SuffixNode
        """
        if self.active_len >= cur_node.edge_label.edge_len():
            self.active_edge += cur_node.edge_label.edge_len()
            self.active_len -= cur_node.edge_label.edge_len()
            self.active_node = cur_node
            return True
        else:
            return False


class SuffixTreeApp:
    def __init__(self, whole_str):
        self.whole_str = whole_str
        self.remaining_count = 0
        self.end_idx = EndIdx()
        self.root_node = SuffixNode(None)
        self.active_point = ActivePoint(self.root_node, -1, 0)

        def build_suffix_tree_via_ukkonen():
            def do_phase_extension(pos):
                self.remaining_count += 1
                self.end_idx.val = pos
                last_new_node = None

                while self.remaining_count > 0:
                    # APCFALZ(active point change for active_len ZERO)
                    if self.active_point.active_len == 0:
                        self.active_point.active_edge = pos

                    edge_first_ch = whole_str[self.active_point.active_edge]
                    if edge_first_ch not in self.active_point.active_node.children_dict:
                        # extension rule 2: create a leaf node
                        self.active_point.active_node.children_dict[edge_first_ch] = SuffixNode(self.root_node, pos,
                                                                                                self.end_idx)
                        if last_new_node is not None:
                            last_new_node.suffix_link = self.active_point.active_node
                            last_new_node = None
                    else:
                        # trick1: skip/count
                        next_node = self.active_point.active_node.children_dict[edge_first_ch]
                        if self.active_point.walk_down_if_possible(next_node):
                            continue  # start from next node(the new active node)

                        # extension rule3, trick2, show stopper, next char being processed is on the edge
                        if whole_str[next_node.edge_label.start_idx + self.active_point.active_len] == whole_str[pos]:
                            if last_new_node is not None:
                                last_new_node.suffix_link = self.active_point.active_node
                                last_new_node = None

                            self.active_point.active_len += 1
                            break

                        # in the middle of edge to split, next char being processed is not on the edge
                        # also in extension rule 2, but create a new leaf node and internal node
                        split_end_idx = EndIdx(next_node.edge_label.start_idx + self.active_point.active_len - 1)
                        split_node = SuffixNode(self.root_node, next_node.edge_label.start_idx, split_end_idx)
                        self.active_point.active_node.children_dict[whole_str[
                            self.active_point.active_edge]] = split_node  # index split_node, instead of next_node

                        # split_node indices its two children
                        split_node.children_dict[whole_str[pos]] = SuffixNode(self.root_node, pos, self.end_idx)
                        next_node.edge_label.start_idx += self.active_point.active_len
                        split_node.children_dict[whole_str[next_node.edge_label.start_idx]] = next_node

                        if last_new_node is not None:
                            last_new_node.suffix_link = split_node

                        last_new_node = split_node

                    self.remaining_count -= 1
                    # active_node is root and active_len is ZERO? this case is already taken care by APCFALZ.
                    if self.active_point.active_node is self.root_node and self.active_point.active_len > 0:
                        self.active_point.active_len -= 1  #
                        self.active_point.active_edge = pos - (self.remaining_count - 1)
                    elif self.active_point.active_node is not self.root_node:
                        self.active_point.active_node = self.active_point.active_node.suffix_link

            def mark_suffix_idx(whole_str_len):
                def dfs_detail(node_ref, cur_path_len):
                    """
                    :type node_ref: SuffixNode
                    """
                    if node_ref.is_leaf():
                        node_ref.suffix_idx = whole_str_len - cur_path_len
                        print node_ref.suffix_idx
                    else:
                        for edge_first_ch in node_ref.children_dict:
                            child_node = node_ref.children_dict[edge_first_ch]
                            dfs_detail(child_node, cur_path_len + child_node.edge_label.edge_len())

                dfs_detail(self.root_node, 0)

            # body of building suffix tree
            for i in xrange(len(whole_str)):
                do_phase_extension(i)

            print 'finish phase computation\n'
            mark_suffix_idx(len(whole_str))
            print 'finish suffix index marking\n'

        build_suffix_tree_via_ukkonen()

    def print_suffix_tree(self):
        def dfs_detail(node_ref, prefix_str, node_level):
            """
            :type node_ref: SuffixNode
            :type prefix_str: str
            :type node_level: int
            """
            blank_str = ''.join(["  "] * node_level)[:-1] + '|_' if node_level > 0 else 'root'
            print '%-50s' % (blank_str + node_ref.edge_label.sub_str(self.whole_str),),
            if node_ref.is_leaf():
                print '(' + prefix_str + ',' + str(node_ref.suffix_idx) + ')'
            else:
                print
                for edge_first_ch in node_ref.children_dict:
                    child_node = node_ref.children_dict[edge_first_ch]
                    dfs_detail(child_node, prefix_str + child_node.edge_label.sub_str(self.whole_str), node_level + 1)

        dfs_detail(self.root_node, "", 0)


if __name__ == '__main__':
    app = SuffixTreeApp("CTGCGT$GTCTGC#")
    app.print_suffix_tree()
