def gcd_euclidean(lhs, rhs):
    if rhs == 0:
        return lhs
    else:
        return gcd_euclidean(rhs, lhs % rhs)


if __name__ == '__main__':
    print ' Demo gcd of 24 and 36' + gcd_euclidean(24, 36);


class InternalStates:
    r_list = list()
    q_list = list()
    x_list = list()
    y_list = list()
    iter_num = -1

    def __init__(self, lhs, rhs):
        self.r_list.append(lhs)
        self.r_list.append(rhs)
        self.q_list.append(None)
        self.q_list.append(None)
        self.x_list.append(1)
        self.x_list.append(0)
        self.y_list.append(0)
        self.y_list.append(1)


def extended_gcd_euclidean(lhs, rhs):
    internal_states = InternalStates();
    return
