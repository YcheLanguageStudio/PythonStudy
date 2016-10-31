import numpy as np
import copy


def init_map(row_num, col_num, map_info):
    map_arr = np.ndarray(shape=(row_num, col_num), dtype=int)
    for i in range(0, len(map_info)):
        row_idx = i / col_num
        col_idx = i % col_num
        if map_info[i] == '0':
            map_arr[row_idx][col_idx] = 0
        else:
            map_arr[row_idx][col_idx] = 1
    return map_arr


def get_connected_number(my_map_arr):
    bfs_mark_num = 0
    copy_map_arr = copy.deepcopy(my_map_arr)
    # print copy_map_arr
    row_num = copy_map_arr.shape[0]
    col_num = copy_map_arr.shape[1]
    start_row_idx = -1
    start_col_idx = -1
    for row_idx in range(0, row_num):
        is_break = False
        for col_idx in range(0, col_num):
            if copy_map_arr[row_idx][col_idx] == 0:
                start_row_idx = row_idx
                start_col_idx = col_idx
                is_break = True
                break
        if is_break:
            break

    frontier_queue = list()
    frontier_queue.append((start_row_idx, start_col_idx))
    copy_map_arr[start_row_idx][start_col_idx] = 2
    while len(frontier_queue) > 0:
        # mark
        start_row_idx = frontier_queue[0][0]
        start_col_idx = frontier_queue[0][1]
        frontier_queue.pop(0)
        bfs_mark_num += 1

        # expand up side
        if start_row_idx - 1 >= 0 and copy_map_arr[start_row_idx - 1][start_col_idx] == 0:
            frontier_queue.append((start_row_idx - 1, start_col_idx))
            copy_map_arr[start_row_idx - 1][start_col_idx] = 2
        # expand down side
        if start_row_idx + 1 < row_num and copy_map_arr[start_row_idx + 1][start_col_idx] == 0:
            frontier_queue.append((start_row_idx + 1, start_col_idx))
            copy_map_arr[start_row_idx + 1][start_col_idx] = 2
        # expand left side
        if start_col_idx - 1 >= 0 and copy_map_arr[start_row_idx][start_col_idx - 1] == 0:
            frontier_queue.append((start_row_idx, start_col_idx - 1))
            copy_map_arr[start_row_idx][start_col_idx - 1] = 2
        # expand right side
        if start_col_idx + 1 < col_num and copy_map_arr[start_row_idx][start_col_idx + 1] == 0:
            frontier_queue.append((start_row_idx, start_col_idx + 1))
            copy_map_arr[start_row_idx][start_col_idx + 1] = 2

    return bfs_mark_num


def get_global_single_exit_num(my_map_arr):
    return -1


def dfs_search(init_row_idx, init_col_idx, marked_num, path_list, my_map_arr):
    my_changed_row_idx = init_row_idx
    my_changed_col_idx = init_col_idx
    max_col_idx = my_map_arr.shape[1] - 1
    max_row_idx = my_map_arr.shape[0] - 1
    whole_num = my_map_arr.shape[0] * my_map_arr.shape[1]

    if marked_num == whole_num:
        return True
    else:
        # prune if there are more than one connected components
        if get_connected_number(my_map_arr) != whole_num - marked_num:
            return False

        # move left
        if init_col_idx - 1 >= 0 and my_map_arr[init_row_idx][init_col_idx - 1] == 0:
            for idx in range(0, init_col_idx)[::-1]:
                if my_map_arr[init_row_idx][idx] == 1:
                    break
                else:
                    my_map_arr[init_row_idx][idx] = 1
                    my_changed_col_idx = idx
                    marked_num += 1

            path_list.append('l')
            if dfs_search(init_row_idx, my_changed_col_idx, marked_num, path_list, my_map_arr):
                return True
            else:
                path_list.pop(len(path_list) - 1)
                for i in range(my_changed_col_idx, init_col_idx):
                    my_map_arr[init_row_idx][i] = 0
                    marked_num -= 1
                my_changed_col_idx = init_col_idx

        # move right
        if init_col_idx + 1 <= max_col_idx and my_map_arr[init_row_idx][init_col_idx + 1] == 0:
            for idx in range(init_col_idx + 1, max_col_idx + 1):
                if my_map_arr[init_row_idx][idx] == 1:
                    break
                else:
                    my_map_arr[init_row_idx][idx] = 1
                    my_changed_col_idx = idx
                    marked_num += 1

            path_list.append('r')
            if dfs_search(init_row_idx, my_changed_col_idx, marked_num, path_list, my_map_arr):
                return True
            else:
                path_list.pop(len(path_list) - 1)
                for i in range(my_changed_col_idx, init_col_idx, -1):
                    my_map_arr[init_row_idx][i] = 0
                    marked_num -= 1

        # move up
        if init_row_idx - 1 >= 0 and my_map_arr[init_row_idx - 1][init_col_idx] == 0:
            for idx in range(0, init_row_idx)[::-1]:
                if my_map_arr[idx][init_col_idx] == 1:
                    break
                else:
                    my_map_arr[idx][init_col_idx] = 1
                    my_changed_row_idx = idx
                    marked_num += 1

            path_list.append('u')
            if dfs_search(my_changed_row_idx, init_col_idx, marked_num, path_list, my_map_arr):
                return True
            else:
                path_list.pop(len(path_list) - 1)
                for i in range(my_changed_row_idx, init_row_idx):
                    my_map_arr[i][init_col_idx] = 0
                    marked_num -= 1
                my_changed_row_idx = init_row_idx

        # move down
        if init_row_idx + 1 <= max_row_idx and my_map_arr[init_row_idx + 1][init_col_idx] == 0:
            for idx in range(init_row_idx + 1, max_row_idx + 1):
                if my_map_arr[idx][init_col_idx] == 1:
                    break
                else:
                    my_map_arr[idx][init_col_idx] = 1
                    my_changed_row_idx = idx
                    marked_num += 1

            path_list.append('d')
            if dfs_search(my_changed_row_idx, init_col_idx, marked_num, path_list, my_map_arr):
                return True
            else:
                path_list.pop(len(path_list) - 1)
                for i in range(my_changed_row_idx, init_row_idx, -1):
                    my_map_arr[i][init_col_idx] = 0
                    marked_num -= 1

        # all not work
        return False


def get_answer_dict(my_row_num, my_col_num, my_map_info):
    ret_dict = str()
    my_map_arr = init_map(my_row_num, my_col_num, my_map_info)
    my_marked_num = len(filter(lambda x: x == '1', my_map_info)) + 1
    for i in range(0, len(my_map_info)):
        tmp_row_idx = i / my_col_num
        tmp_col_idx = i % my_col_num
        print tmp_row_idx, tmp_col_idx
        tmp_list = list()
        if my_map_arr[tmp_row_idx][tmp_col_idx] == 0:
            new_map_arr = copy.deepcopy(my_map_arr)
            new_map_arr[tmp_row_idx][tmp_col_idx] = 1
            if dfs_search(tmp_row_idx, tmp_col_idx, my_marked_num, tmp_list, new_map_arr):
                print 'find it'
                ret_dict = 'x=' + str(tmp_row_idx + 1) + '&y=' + str(tmp_col_idx + 1) + '&path=' + ''.join(tmp_list)
                break
    return ret_dict


if __name__ == '__main__':
    my_map_str = '000110000100000000000000110100001100000100100000100101000111100001000010000001000100011110000100000001110000110000001000000100010001100100100010101000000100010001100010001000100000000100001011110011000010001000011000000111110000001000000000011001111100010001000010000000111100010001000010000011000001010000000110100110000100010001100000100001100100000000000010101001000001001000100010001000001100011000100010000110011000010000000100000111111100010001000100000111001111010100000100110000010011010100001101100000010000100100001000011110000000100011001110001110011010000001110001100000100010000101000000011001100010000100010010'
    my_row_num_int = 24
    my_col_num_int = 26

    my_dict = get_answer_dict(my_row_num_int, my_col_num_int, my_map_str)
    print my_dict
