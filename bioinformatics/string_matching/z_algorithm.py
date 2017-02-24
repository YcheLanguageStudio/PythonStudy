unique_character = '$'


def z_algorithm_detail(super_str, pat_size):
    z_score_arr = [0] * len(super_str)
    l, r = 0, 0

    def get_match_num(begin_0, begin_1):
        match_num = 0
        while super_str[begin_0 + match_num] == super_str[begin_1 + match_num]:
            match_num += 1
        return match_num

    for k in xrange(1, len(super_str)):
        if k > r:
            match_num = get_match_num(begin_0=k, begin_1=0)
            z_score_arr[k] = match_num
            if match_num > 0:
                l, r = k, k + match_num - 1
        else:
            k_prime = k - l
            beta = r - k + 1
            if z_score_arr[k_prime] < beta:
                z_score_arr[k] = z_score_arr[k_prime]
            elif z_score_arr[k_prime] > beta:
                z_score_arr[k] = beta
            else:
                match_num = get_match_num(begin_0=r + 1, begin_1=r - k + 1)
                z_score_arr[k] = beta + match_num
                if match_num > 0:
                    l, r = k, k + z_score_arr[k] - 1

    return filter(lambda idx: z_score_arr[idx] == pat_size, range(len(super_str)))


def search_pattern_str_z(pat, txt):
    match_list = z_algorithm_detail(pat + unique_character + txt, len(pat))
    return map(lambda idx: idx - len(pat + unique_character), match_list)


def search_pattern_str_naive(pat, txt):
    return filter(lambda i: txt[i:i + len(pat)] == pat, range(len(txt) - len(pat) + 1))


if __name__ == '__main__':
    pat = 'aba'
    txt = 'bbabaxababay'
    print 'naive:', search_pattern_str_naive(pat, txt)
    print 'z algorithm:', search_pattern_str_z(pat, txt)
