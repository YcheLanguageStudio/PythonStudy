import itertools

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
    return filter(lambda idx: z_score_arr[idx] == pat_size, range(len(super_str))), z_score_arr


def search_pattern_str_z(pat, txt):
    match_list, z_score_arr = z_algorithm_detail(pat + unique_character + txt, len(pat))
    return map(lambda idx: idx - len(pat + unique_character), match_list), z_score_arr


def search_pattern_str_naive(pat, txt):
    return filter(lambda i: txt[i:i + len(pat)] == pat, range(len(txt) - len(pat) + 1))


def test_cases():
    pat = 'aba'
    txt = 'bbabaxababay'
    print 'naive:', search_pattern_str_naive(pat, txt)
    print 'z algorithm:' + str(search_pattern_str_z(pat, txt)) + '\n'


def solve_homework4():
    pat = 'GC'
    txt = 'GCTTGGCATA'
    print 'naive:', search_pattern_str_naive(pat, txt)
    print 'z algorithm:' + str(search_pattern_str_z(pat, txt)) + '\n'

    alphabet = ['A', 'G', 'C', 'T']
    wild_card_pat = 'G*'

    def expand_wildcard_character(wildcard_str):
        combinations = map(lambda my_tuple: ''.join(my_tuple),
                           list(apply(itertools.product,
                                      tuple(map(lambda ch: alphabet if ch == '*' else [ch], wildcard_str)))))
        return combinations

    z_score_arr_list = []
    idx_list_set = set()
    for pat in expand_wildcard_character(wild_card_pat):
        print 'pat:', pat
        print 'naive:', search_pattern_str_naive(pat, txt)
        idx_list, z_score_arr = search_pattern_str_z(pat, txt)
        print 'z algorithm:' + str((idx_list, z_score_arr)) + '\n'
        z_score_arr_list.append(z_score_arr)
        idx_list_set |= set(idx_list)

    final_z_score_arr = reduce(lambda l, r: map(lambda my_pair: max(my_pair[0], my_pair[1]), zip(l, r)),
                               z_score_arr_list, z_score_arr_list[0])
    print idx_list_set, final_z_score_arr


if __name__ == '__main__':
    test_cases()
    solve_homework4()
