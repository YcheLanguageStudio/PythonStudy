# depth starts from zero
def fixed_depth_search(min_cells_to_add, depth, ref_pieces_list, ref_map_arr):
    if depth == len(ref_pieces_list):
        return True
    ref_expand_piece = ref_pieces_list[depth]
    cur_piece_row_num = len(ref_expand_piece)
    cur_piece_col_num = len(ref_expand_piece[0])
