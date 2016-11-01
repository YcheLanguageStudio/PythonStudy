def cal_left_nums_count(ref_map_arr):
    count = 0
    for row in ref_map_arr:
        for col_val in row:
            count += col_val
    return count


def fixed_depth_search(depth, left_cells, ref_path_list, ref_pieces_list, ref_piece_sum_list, ref_map_arr, modulo_num):
    left_nums_count = cal_left_nums_count(ref_map_arr)

    if depth == len(ref_pieces_list):
        if left_nums_count == 0:
            return True
        else:
            return False
    else:
        # do pruning
        left_cells -= ref_piece_sum_list[depth]
        if left_cells < left_nums_count:
            return False

    ref_expand_piece = ref_pieces_list[depth]
    cur_piece_row_num = len(ref_expand_piece)
    cur_piece_col_num = len(ref_expand_piece[0])
    max_row_idx = len(ref_map_arr) - 1
    max_col_idx = len(ref_map_arr[0]) - 1

    for start_row_idx in range(0, max_row_idx - cur_piece_row_num + 2):
        for start_col_idx in range(0, max_col_idx - cur_piece_col_num + 2):
            ref_path_list.append((start_row_idx, start_col_idx))
            print start_row_idx, start_col_idx
            # do overlapping
            for local_row_idx in range(0, cur_piece_row_num - 1):
                for local_col_idx in range(0, cur_piece_col_num - 1):
                    ref_map_arr[start_row_idx + local_row_idx][start_col_idx + local_col_idx] += \
                        ref_expand_piece[local_row_idx][local_col_idx]
                    ref_map_arr[start_row_idx + local_row_idx][start_col_idx + local_col_idx] %= modulo_num
            if fixed_depth_search(depth + 1, left_cells, ref_path_list, ref_pieces_list,
                                  ref_piece_sum_list, ref_map_arr, modulo_num):
                return True
            else:
                # revert overlapping
                ref_path_list.pop(len(ref_path_list) - 1)
                for local_row_idx in range(0, cur_piece_row_num - 1):
                    for local_col_idx in range(0, cur_piece_col_num - 1):
                        ref_map_arr[start_row_idx + local_row_idx][start_col_idx + local_col_idx] += \
                            modulo_num - ref_expand_piece[local_row_idx][local_col_idx]
                        ref_map_arr[start_row_idx + local_row_idx][start_col_idx + local_col_idx] %= modulo_num
    return False
