def min_num_coin(coin_list, val):
    coin_list = sorted(set(coin_list), key=lambda x: -x)
    choice_list = []

    # key: end_idx, val: (min_coin_num, path)
    min_coin_num_dict = {}

    def min_num_coin_detail(end_idx, left_val, coin_count, path):
        if end_idx in min_coin_num_dict:
            return min_coin_num_dict[end_idx][0]
        else:
            if left_val == 0:
                return coin_count
            elif end_idx == 0:
                if left_val % coin_list[0] != 0:
                    return val + 1
                else:
                    return coin_count + left_val / coin_list[0]


if __name__ == '__main__':
    lst = [1, 2]
    print lst + [3, 4]
