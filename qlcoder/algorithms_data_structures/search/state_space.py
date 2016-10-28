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
        print ''.join(path_list)
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
        if init_col_idx + 1 <= max_row_idx and my_map_arr[init_row_idx][init_col_idx + 1] == 0:
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


if __name__ == '__main__':
    my_map_info = '00000000000000000001000010000000000'
    my_marked_num = len(filter(lambda x: x == '1', my_map_info))
    my_row_num = 5
    my_col_num = 7
    my_map_arr = init_map(my_row_num, my_col_num, my_map_info)

    for i in range(0, len(my_map_info)):
        tmp_row_idx = i / my_col_num
        tmp_col_idx = i % my_col_num
        print tmp_row_idx, tmp_col_idx
        tmp_list = list()
        if my_map_arr[tmp_row_idx][tmp_col_idx] == 0:
            if dfs_search(tmp_row_idx, tmp_col_idx, my_marked_num, tmp_list, copy.copy(my_map_arr)):
                print tmp_list
                break
