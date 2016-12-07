import copy
from extended_euclidean import ExtendedGcdEuclidean


def compute_multiplicative_inverse(modulo_num, another_num):
    algorithm = ExtendedGcdEuclidean(modulo_num=modulo_num, another_num=another_num)
    return algorithm.get_result()


class ChineseRemainder:
    def __init__(self, pairwise_prime_nums):
        self.arr_m = pairwise_prime_nums
        self.M = reduce(lambda left, right: left * right, pairwise_prime_nums, 1)
        self.arr_M = map(lambda ele: self.M / ele, self.arr_m)
        self.arr_mul_inverse_M = map(lambda ele: compute_multiplicative_inverse(ele, self.M / ele), self.arr_m)

    def get_remainder_list(self, num):
        return map(lambda ele: num % ele, self.arr_m)

    def get_original_number(self, remainder_lst):
        sum_num = 0
        for i in range(len(remainder_lst)):
            sum_num += remainder_lst[i] * self.arr_M[i] * self.arr_mul_inverse_M[i]
        return sum_num % self.M


def list_add(left_list, right_list):
    new_list = copy.deepcopy(left_list)
    if len(left_list) != len(right_list):
        print 'error'
        return None
    else:
        for i in range(len(right_list)):
            new_list[i] += right_list[i]
        return new_list

