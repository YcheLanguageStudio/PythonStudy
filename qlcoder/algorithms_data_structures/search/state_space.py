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


def dfs_search(init_row_idx, init_col_idx, marked_num, path_list, my_map_arr):
    my_changed_row_idx = init_row_idx
    my_changed_col_idx = init_col_idx
    max_col_idx = my_map_arr.shape[1] - 1
    max_row_idx = my_map_arr.shape[0] - 1
    whole_num = my_map_arr.shape[0] * my_map_arr.shape[1]

    if marked_num == whole_num:
        return True
    else:
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
        print tmp_row_idx,tmp_col_idx
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
    my_map_str = '111000010000000100010010110000111100010100001100100110000001011000000100001111000000100001000000110011000011000000100000111100000000100000001110000010100001110000100000001001000000001000010001000001100000100001010011010001100010000111110001000000100000100000110001000001100011100101000101011100000001011101010000110000000001000000101000011011000000001000110000'
    my_row_num_int = 18
    my_col_num_int = 20

    my_dict = get_answer_dict(my_row_num_int, my_col_num_int, my_map_str)
    print my_dict
