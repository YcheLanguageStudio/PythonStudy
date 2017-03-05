class EndIdx:
    def __init__(self):
        self.val = -1

    def __add__(self, other):
        self.val += other


class SuffixNode:
    class InEdgeLabel:
        def __init__(self, start_idx=-1, end_idx_ref=None):
            self.start_idx = start_idx
            self.end_idx_ref = end_idx_ref

        def edge_len(self):
            assert isinstance(self.end_idx_ref, EndIdx)
            return self.end_idx_ref.val - self.start_idx

    def __init__(self, suffix_ref=None, start_idx=-1, end_idx_ref=None, suffix_idx=-1):
        self.children_dict = {}
        self.suffix_ref = suffix_ref
        self.edge_label = SuffixNode.InEdgeLabel(start_idx, end_idx_ref)
        self.suffix_idx = suffix_idx


class ActivePoint:
    def __init__(self, active_node, active_edge, active_len):
        self.active_node = active_node
        self.active_edge = active_edge
        self.active_len = active_len

    def walk_down(self, cur_suffix_node):
        """
        :type cur_suffix_node: SuffixNode
        """
        if self.active_len >= cur_suffix_node.edge_label.edge_len():
            self.active_edge += cur_suffix_node.edge_label.edge_len()
            self.active_len -= cur_suffix_node.edge_label.edge_len()
            self.active_node = cur_suffix_node


class UkknonenAlgorithm:
    def __init__(self, whole_str):
        print

    def build_suffix_tree(self, whole_str):
        def do_phase_extension(pos):
            return

        return
