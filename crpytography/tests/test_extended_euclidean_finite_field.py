from crpyto_tool.libs.extended_euclidean_poly import *
from crpyto_tool.libs.finite_field_op import FiniteFieldNumber


def test_extended_gcd_eculidean(modulo_num, another_num):
    extend_euclidean_algo = ExtendedGcdEuclidean(modulo_num, another_num)
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


if __name__ == '__main__':
    px_number = FiniteFieldNumber(FiniteFieldNumber.magical_number, False)

    ax_number0 = FiniteFieldNumber('10000011')
    test_extended_gcd_eculidean(px_number, ax_number0)

    print '\n'

    ax_number1 = FiniteFieldNumber('1000110')
    test_extended_gcd_eculidean(px_number, ax_number1)
