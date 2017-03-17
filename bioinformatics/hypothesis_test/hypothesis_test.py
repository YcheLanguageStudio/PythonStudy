if __name__ == '__main__':
    observed_list = [233, 385, 129]

    p = float(observed_list[0] * 2 + observed_list[1]) / (sum(observed_list) * 2)
    q = float(observed_list[2] * 2 + observed_list[1]) / (sum(observed_list) * 2)
    print p, q
    expected_freq_list = [p ** 2, 2 * p * q, q ** 2]

    observed_freq_list = map(lambda num: float(num) / 747, observed_list)
    print 'observed:', observed_freq_list
    print 'expected:', expected_freq_list

    print sum(observed_list) * sum(
        map(lambda pair: (pair[0] - pair[1]) ** 2 / pair[1], zip(observed_freq_list, expected_freq_list)))
