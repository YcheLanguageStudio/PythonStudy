from finite_field_op import FiniteFieldNumber


class ExtendedGcdEuclidean:
    def __init__(self, modulo_num, another_num):
        self.r_list = list([modulo_num, another_num])
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


