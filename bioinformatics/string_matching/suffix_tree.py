class EndIdx:
    def __init__(self, val=-1):
        self.val = val


class SuffixNode:
    class InEdgeLabel:
        def __init__(self, start_idx=-1, end_idx_ref=None):
            self.start_idx = start_idx
            self.end_idx_ref = end_idx_ref

        def edge_len(self):
            assert isinstance(self.end_idx_ref, EndIdx)
            return self.end_idx_ref.val - self.start_idx

    def __init__(self, start_idx=-1, end_idx_ref=None, suffix_ref=None, suffix_idx=-1):
        self.children_dict = {}
        self.suffix_ref = suffix_ref
        self.edge_label = SuffixNode.InEdgeLabel(start_idx, end_idx_ref)
        self.suffix_idx = suffix_idx


class ActivePoint:
    def __init__(self, active_node, active_edge, active_len):
        """
        :type active_node: SuffixNode
        """
        self.active_node = active_node
        self.active_edge = active_edge
        self.active_len = active_len

    def walk_down_if_possible(self, cur_suffix_node):
        """
        :type cur_suffix_node: SuffixNode
        """
        if self.active_len >= cur_suffix_node.edge_label.edge_len():
            self.active_edge += cur_suffix_node.edge_label.edge_len()
            self.active_len -= cur_suffix_node.edge_label.edge_len()
            self.active_node = cur_suffix_node


class UkknonenAlgorithm:
    def __init__(self, whole_str):
        self.remaining_count = 0
        self.end_idx = EndIdx()
        self.root_node = SuffixNode()
        self.active_point = ActivePoint(self.root_node, -1, 0)
        self.build_suffix_tree(whole_str)

    def build_suffix_tree(self, whole_str):
        def do_phase_extension(pos):
            self.remaining_count += 1
            self.end_idx.val = pos
            last_new_node = None
            while self.remaining_count > 0:
                if self.active_point.active_len == 0:
                    self.active_point.active_edge = pos

                edge_first_ch = whole_str[self.active_point.active_edge]
                if edge_first_ch not in self.active_point.active_node.children_dict:
                    self.active_point.active_node.children_dict[edge_first_ch] = SuffixNode(pos, self.end_idx,
                                                                                            self.root_node)
                    if last_new_node is not None:
                        last_new_node.suffix_ref = self.active_point.active_node
                        last_new_node = None
                else:
                    next_node = self.active_point.active_node.children_dict[edge_first_ch]
                    self.active_point.walk_down_if_possible(next_node)

                    if whole_str[next_node.edge_label.start_idx + self.active_point.active_len] == whole_str[pos]:
                        if last_new_node is not None:
                            last_new_node.suffix_ref = self.active_point.active_node
                            last_new_node = None

                        self.active_point.active_len += 1
                        break

                    # in the middle of edge to split
                    split_end_idx = EndIdx(next_node.edge_label.start_idx + self.active_point.active_len - 1)
                    split_node = SuffixNode(next_node.edge_label.start_idx, split_end_idx)
                    self.active_point.active_node.children_dict[whole_str[self.active_point.active_edge]] = split_node

                    split_node.children_dict[whole_str[pos]] = SuffixNode(pos, self.end_idx, self.root_node)
                    next_node.edge_label.start_idx += self.active_point.active_len
                    split_node.children_dict[whole_str[next_node.edge_label.start_idx]] = next_node

                    if last_new_node is not None:
                        last_new_node.suffix_ref = split_node

                    last_new_node = split_node

                self.remaining_count -= 1
                if self.active_point.active_node is self.root_node and self.active_point.active_len > 0:
                    self.active_point.active_len -= 1
                    self.active_point.active_edge = pos - self.remaining_count + 1
                elif self.active_point.active_node is not self.root_node:
                    self.active_point.active_node = self.active_point.active_node.suffix_ref

        for i in xrange(len(whole_str)):
            do_phase_extension(i)


if __name__ == '__main__':
    root_node = UkknonenAlgorithm("AAAGTGCTCAATGAAAAGGAA").root_node
