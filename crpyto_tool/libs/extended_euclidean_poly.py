from finite_field_op import FiniteFieldNumber


class ExtendedGcdEuclidean:
    def __init__(self, lhs, rhs):
        self.r_list = list([lhs, rhs])
        self.q_list = list([None, None])
        self.x_list = list([FiniteFieldNumber(1, False), FiniteFieldNumber(0, False)])
        self.y_list = list([FiniteFieldNumber(0, False), FiniteFieldNumber(1, False)])
        self.iter_list = list([-1, 0])
        self.is_break = False
        self.compute_final_result()

    def do_one_iteration(self):
        next_tail_index = len(self.iter_list)
        self.iter_list.append(self.iter_list[next_tail_index - 1] + 1)
        self.q_list.append(self.r_list[next_tail_index - 2] / self.r_list[next_tail_index - 1])
        self.r_list.append(self.r_list[next_tail_index - 2] % self.r_list[next_tail_index - 1])

        if self.r_list[next_tail_index].integer_32bits == 0:
            self.is_break = True
        else:
            self.x_list.append(self.x_list[next_tail_index - 2] -
                               self.q_list[next_tail_index] * self.x_list[next_tail_index - 1])
            self.y_list.append(self.y_list[next_tail_index - 2] -
                               self.q_list[next_tail_index] * self.y_list[next_tail_index - 1])

    def compute_final_result(self):
        while not self.is_break:
            self.do_one_iteration()


def test_extended_gcd_eculidean(lhs, rhs):
    extend_euclidean_algo = ExtendedGcdEuclidean(lhs, rhs)
    for i in range(0, len(extend_euclidean_algo.iter_list) - 1):
        print 'iter:' + str(extend_euclidean_algo.iter_list[i]) + '\t\tr:' + \
              str(extend_euclidean_algo.r_list[i]) + '\t\tq:' + \
              str(extend_euclidean_algo.q_list[i]) + '\t\tx:' + \
              str(extend_euclidean_algo.x_list[i]) + \
              '\t\ty:' + str(extend_euclidean_algo.y_list[i])

    i = len(extend_euclidean_algo.iter_list) - 1

    print 'iter:' + str(extend_euclidean_algo.iter_list[i]) + '\t\tr:' \
          + str(extend_euclidean_algo.r_list[i]) + '\t\tq:' \
          + str(extend_euclidean_algo.q_list[i])


