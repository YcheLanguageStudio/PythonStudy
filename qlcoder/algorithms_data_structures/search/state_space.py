import numpy as np


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


def dfs_search(init_row_idx, init_col_idx, marked_num, whole_num, path_list, my_map_arr):
    my_changed_row_idx = init_row_idx
    my_changed_col_idx = init_col_idx
    if marked_num == whole_num:
        print ''.join(path_list)
        return True
    else:
        if init_col_idx - 1 >= 0 and my_map_arr[init_row_idx][init_col_idx - 1] == 0:
            for i in range(1, init_col_idx + 1):
                if my_map_arr[init_col_idx - i] == 1:
                    break
                else:
                    my_changed_row_idx -= 1
                    my_map_arr[init_row_idx][my_changed_col_idx] = 1
                    marked_num += 1
            path_list.append('l')
            if (dfs_search(my_changed_row_idx, my_changed_col_idx, marked_num, whole_num,
                           path_list, my_map_arr) == True):
                return True

        # change state for left
        # if ok
        # if(dfs_search())

        # change state for left
        # if ok
        # if(dfs_search())
        return False


if __name__ == '__main__':
    my_map_info = '00000000000000000001000010000000000'
    my_marked_num = len(filter(lambda x: x == '1', my_map_info))
    my_row_num = 5
    my_col_num = 7
    my_map_arr = init_map(my_row_num, my_col_num, my_map_info)
    print my_map_arr.shape[0]
    print my_map_arr.shape[1]
