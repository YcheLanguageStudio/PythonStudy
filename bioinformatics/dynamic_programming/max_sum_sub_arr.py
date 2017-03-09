import numpy as np


def inclusive_scan(num_list):
    ret_list = []
    sum_val = 0
    for num in num_list:
        sum_val += num
        ret_list.append(sum_val)
    return ret_list


# inclusive i, j
def min_max(i, j, num_list):
    assert 0 <= i <= j <= len(num_list)
    min_idx, max_idx = i, i
    min_val, max_val = num_list[i], num_list[i]
    for idx in xrange(i + 1, j + 1):
        if min_val > num_list[idx]:
            min_idx, min_val = idx, num_list[idx]
        if max_val < num_list[idx]:
            max_idx, max_val = idx, num_list[idx]
    return min_idx, max_idx


def max_difference(i, j, num_list):
    # condition
    if i > j:
        return -1, -1, -np.inf
    else:
        min_idx, max_idx = min_max(i, j, num_list)
        if min_idx <= max_idx:
            return min_idx, max_idx, num_list[max_idx] - num_list[min_idx]
        else:
            cur_min_idx, cur_max_idx = min_max(i, max_idx, num_list)
            cur_max_differ = num_list[cur_max_idx] - num_list[cur_min_idx]

            new_min_idx, new_max_idx = min_max(min_idx, j, num_list)
            new_max_differ = num_list[new_max_idx] - num_list[new_max_idx]

            if new_max_differ > cur_max_differ:
                cur_min_idx, cur_max_idx = new_min_idx, new_max_idx

            middle_min_idx, middle_max_idx, middle_max_differ = max_difference(max_idx + 1, min_idx - 1, num_list)
            if middle_max_differ > cur_max_differ:
                cur_min_idx, cur_max_idx, cur_max_differ = middle_min_idx, middle_max_idx, middle_max_differ

            return cur_min_idx, cur_max_idx, cur_max_differ


if __name__ == '__main__':
    input_list = [1, -2, 3, 10, -4, 7, 2, -5]
    scan_list = inclusive_scan(input_list)
    print input_list
    print scan_list
    print max_difference(0, len(scan_list) - 1, scan_list)

    scan_list1 = [2, 4, 7, -1, 3, 6, -2, 4]
    print max_difference(0, len(scan_list1)-1, scan_list1)