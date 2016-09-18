def gcd_euclidean(lhs, rhs):
    if rhs == 0:
        return lhs
    else:
        return gcd_euclidean(rhs, lhs % rhs)


if __name__ == '__main__':
    print ' Demo gcd of 24 and 36' + gcd_euclidean(24, 36);


def extended_gcd_euclidean(lhs, rhs, four_lists):
    return

