# depth starts from zero
def fixed_depth_search(min_cells_to_add, depth, pieces_list):
    if depth == len(pieces_list):
        return True
    