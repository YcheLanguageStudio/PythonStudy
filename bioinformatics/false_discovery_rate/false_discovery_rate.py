import math


def nCr(n, r):
    f = math.factorial
    return f(n) / f(r) / f(n - r)


def compute_expectation(alpha, beta, truth_true_num, truth_false_num):
    sum_val = 0
    for a in xrange(1, truth_true_num + 1):
        for b in xrange(0, truth_false_num + 1):
            sum_val += float(a) / (a + b) \
                       * nCr(truth_true_num, a) * (alpha ** a) * ((1 - alpha) ** (truth_true_num - a)) \
                       * nCr(truth_false_num, b) * (beta ** b) * ((1 - beta) ** (truth_false_num - b))
    return sum_val


def compute_expectation2(alpha, beta, truth_true_num, truth_false_num):
    return float(alpha * truth_true_num) / (alpha * truth_true_num + beta * truth_false_num)


if __name__ == '__main__':
    print sum([1.0 / (i + 1) for i in range(100)])

    print compute_expectation(alpha=0.2, beta=0.9, truth_true_num=2, truth_false_num=1)
    print compute_expectation2(alpha=0.2, beta=0.9, truth_true_num=2, truth_false_num=1)

    print compute_expectation(alpha=0.2, beta=0.9, truth_true_num=20, truth_false_num=10)
    print compute_expectation2(alpha=0.2, beta=0.9, truth_true_num=20, truth_false_num=10)
