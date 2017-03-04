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


class PhaseInfo:
    def __init__(self, last_new_node, active_node):
        self.last_new_node = last_new_node
        self.active_node = active_node


class ActiveInfo:
    def __init__(self, active_node, active_edge, active_len):
        self.active_node = active_node
        self.active_edge = active_edge
        self.active_len = active_len
