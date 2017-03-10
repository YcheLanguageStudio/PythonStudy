def count_bits(num):
    ret_list = [0 for _ in range(num + 1)]
    num_arr = [0 for _ in range(num + 1)]

    def count_and_flip():
        count = 0
        cur_idx = 0
        for idx in xrange(0, len(num_arr)):
            if num_arr[idx] == 1:
                num_arr[idx] = 0
                cur_idx = idx
                count += 1
            else:
                break
        num_arr[cur_idx + 1] = 1
        return count - 1

    for i in xrange(1, len(num_arr)):
        if num_arr[0] == 0:
            ret_list[i] = ret_list[i - 1] + 1
            num_arr[0] = 1
        else:
            ret_list[i] = ret_list[i - 1] - count_and_flip()
    return ret_list


if __name__ == '__main__':
    print count_bits(5)
