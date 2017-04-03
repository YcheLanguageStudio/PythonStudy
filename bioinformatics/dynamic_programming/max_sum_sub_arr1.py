def max_sum_sub_arr(arr):
    score_vector = [0 for _ in range(len(arr))]

    def max_sum_sub_arr_detail(beg_idx):
        if beg_idx >= len(arr):
            return 0
        elif arr[beg_idx] >= 0:
            score_vector[beg_idx] = arr[beg_idx] + max_sum_sub_arr_detail(beg_idx + 1)
            return score_vector[beg_idx]
        else:
            score_vector[beg_idx] = max(0, arr[beg_idx] + max_sum_sub_arr_detail(beg_idx + 1))
            return score_vector[beg_idx]

    max_sum_sub_arr_detail(0)
    print score_vector
    return max(score_vector)


if __name__ == '__main__':
    print max_sum_sub_arr([1, -2, 3, 10, -4, 7, 2, -5])
